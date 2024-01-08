import fnmatch
import os
import re
import subprocess
from typing import List

import array_gen
import matplotlib.pyplot as plt
import numpy as np

array_dir = "arrays"
graph_dir = "graphs"
graph_ext = ".png"
MAX_32_BIT = 2147483645
MIN_32_BIT = -2147483645

nb_calls = 1
# array_size = 10000
array_sizes = [10, 100, 500, 1000, 2500, 5000, 10000]
spreads = [10, 100, 200, 500, 1000, 5000, 10000]
array_functions = [
    array_gen.randoms,
    array_gen.random_even,
    array_gen.random_uneven,
    array_gen.random_prime,
    array_gen.worst_case,
]


def get_graph_name(array_size: int, min: int, max: int, function):
    s = "Taille Tableau: "
    s1 = str(array_size)
    s2 = ", Valeurs: "
    s3 = str(min)
    s4 = "-"
    s5 = str(max)
    s6 = ", Fonction: "
    s7 = str(function)
    debut_nom = s7.find(" ") + 1
    fin_nom = s7.find(" at")
    s7 = s7[debut_nom:fin_nom]
    return s + s1 + s2 + s3 + s4 + s5 + s6 + s7


def search_algorithms():
    folder = "lib"
    extension = ".so"
    files = []
    # Parcours du dossier
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, "libmerge_sort" + extension):
            filename = os.path.splitext(filename)[0][3:]
            files.append(filename)
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, "libcomb_sort" + extension):
            filename = os.path.splitext(filename)[0][3:]
            files.append(filename)
    return files


def get_diagram(filename, title, xlabel, ylabel, xdata, ydata):
    plt.bar(ydata, xdata, color="blue", width=0.7, bottom=0)
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
    plt.savefig(graph_dir + "/" + filename + graph_ext)


def get_plot(filename, title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
    plt.savefig(graph_dir + "/" + filename + graph_ext)


# get avg/file:
def get_avg_per_file(results):
    avg: List = [0 for _ in range(len(files))]
    total: List = [0 for _ in range(len(files))]
    for i in range(len(results)):
        for j in range(len(results[i])):
            total[j] += results[i][j][1]

    for i in range(len(total)):
        avg[i] = total[i] / (len(results) / len(files))
    return avg


# get avg per arraysize for an alg:
# index = files[x] = un algorithme
def get_avg_per_arrsize(results, array_sizes, index):
    nb_results = len(results) / len(array_sizes)
    total: List = [0 for _ in range(len(array_sizes))]
    avg: List = [0 for _ in range(len(array_sizes))]
    j = 0
    tmp = 0
    for i in range(len(results)):
        total[j] += results[i][index][1]
        tmp += 1
        if tmp >= nb_results:
            tmp = 0
            j += 1
    for i in range(len(array_sizes)):
        avg[i] = total[i] / (len(results) / len(array_sizes))
    return avg


def get_avg_per_spread(results, spreads, index):
    nb_results = len(results) / len(spreads)
    total: List = [0 for _ in range(len(spreads))]
    avg: List = [0 for _ in range(len(spreads))]
    j = 0
    tmp = 0
    for i in range(len(results)):
        total[j] += results[i][index][1]
        tmp += 1
        if tmp >= nb_results:
            tmp = 0
            j += 1
    for i in range(len(spreads)):
        avg[i] = total[i] / (len(results) / len(spreads))
    return avg


def get_avg_per_valuetype(results, functions, index):
    nb_results = len(results) / len(functions)
    total: List = [0 for _ in range(len(functions))]
    avg: List = [0 for _ in range(len(functions))]
    j = 0
    tmp = 0
    for i in range(len(results)):
        total[j] += results[i][index][1]
        tmp += 1
        if tmp >= nb_results:
            tmp = 0
            j += 1
    for i in range(len(functions)):
        avg[i] = total[i] / (len(results) / len(functions))
    return avg


def call_c_program(algorithm_name, array_size):
    cmd = ["bin/main", algorithm_name, str(array_size)]
    sortie = subprocess.check_output(cmd, shell=False)
    temps_match = re.search(
        r"Temps d'exécution : (\d+\.\d+) secondes", sortie.decode("utf-8")
    )
    if temps_match:
        return float(temps_match.group(1))
    else:
        print("Erreur : impossible de trouver le temps d'éxécution dans la sortie.")
        return -1


# retourne le temps d'éxécution moyen de chaque algo dans une liste
def benchmark(files, array_size, array_function, min, max):
    array_gen.write_csv(array_function(array_size, min, max), array_dir)
    tmp_temps_execution = []
    temps_execution = []
    for i in range(len(files)):
        for _ in range(nb_calls):
            cmd = ["bin/main", files[i], str(array_size)]
            sortie = subprocess.check_output(cmd, shell=False)
            temps_match = re.search(
                r"Temps d'exécution : (\d+\.\d+) secondes", sortie.decode("utf-8")
            )
            if temps_match:
                tmp_temps_execution.append(float(temps_match.group(1)))
            else:
                print(
                    "Erreur : impossible de trouver le temps d'éxécution dans la sortie."
                )

            avg = 0.0
            for j in tmp_temps_execution:
                avg += j

        avg = avg / len(tmp_temps_execution)
        temps_execution.append(avg)
    return temps_execution


# temps exec moyen de chaque algo
def bench_file(array_size, spread, array_function):
    temps_execution = []
    for i in range(len(files)):
        tmp_temps_execution = []
        arr = array_function(array_size, 0, spread)
        array_gen.write_csv(arr, array_dir)
        for _ in range(nb_calls):
            res = call_c_program(files[i], array_size)
            tmp_temps_execution.append(res)
        avg = 0.0
        for k in tmp_temps_execution:
            avg += k
        avg = avg / len(tmp_temps_execution)
        temps_execution.append(avg)
    return temps_execution


# temps d'exec moyen de chaque array_sizes
def bench_arrsize(algorithm, spread, array_function):
    temps_execution = []
    for i in range(len(array_sizes)):
        tmp_temps_execution = []
        arr = array_function(array_sizes[i], 0, spread)
        array_gen.write_csv(arr, array_dir)
        for _ in range(nb_calls):
            res = call_c_program(algorithm, array_sizes[i])
            tmp_temps_execution.append(res)
        avg = 0.0
        for k in tmp_temps_execution:
            avg += k
        avg = avg / len(tmp_temps_execution)
        temps_execution.append(avg)
    return temps_execution


# retourne le temps d'execution de chaque spreads
def bench_spread(algorithm, array_size, array_function):
    temps_execution = []
    for i in range(len(spreads)):
        tmp_temps_execution = []
        arr = array_function(array_size, 0, spreads[i])
        array_gen.write_csv(arr, array_dir)
        for _ in range(nb_calls):
            res = call_c_program(algorithm, array_size)
            tmp_temps_execution.append(res)
        avg = 0.0
        for k in tmp_temps_execution:
            avg += k
        avg = avg / len(tmp_temps_execution)
        temps_execution.append(avg)
    return temps_execution


# temps d'execution de chaque array_functions
def bench_array_func(algorithm, array_size, spread):
    temps_execution = []
    for i in range(len(array_functions)):
        tmp_temps_execution = []
        arr_func = array_functions[i]
        arr = arr_func(array_size, 0, spread)
        array_gen.write_csv(arr, array_dir)
        for _ in range(nb_calls):
            res = call_c_program(algorithm, array_size)
            tmp_temps_execution.append(res)
        avg = 0.0
        for k in tmp_temps_execution:
            avg += k
        avg = avg / len(tmp_temps_execution)
        temps_execution.append(avg)
    return temps_execution


def run_bench_on_arrsizes(files):
    for file in files:
        results = []
        for spread in spreads:
            for array_func in array_functions:
                res = bench_arrsize(file, spread, array_func)
                results.append(res)

        avgs = [0] * len(results[0])
        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        avgs = [avg / len(results) for avg in avgs]
        plt.plot(array_sizes, avgs, label=file)
        get_plot(
            "avg_per_arrsize",
            "Temps moyen d'execution en fonction de la taille du tableau",
            "Taille Tableau",
            "Temps",
        )


def run_bench_on_spreads(files):
    results = []
    for file in files:
        for size in array_sizes:
            for function in array_functions:
                res = bench_spread(file, size, function)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        avgs = [avg / len(results) for avg in avgs]
        plt.plot(spreads, avgs, label=file)
        get_plot(
            "avg_per_spread",
            "Temps moyen d'execution en fonction de la fourchette de valeurs",
            "Fourchette",
            "Temps",
        )


def run_bench_on_valuetype(files):
    results = []
    for file in files:
        for size in array_sizes:
            for spread in spreads:
                res = bench_array_func(file, size, spread)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        plt.plot(str_array_functions, avgs, label=file, marker="o", linestyle="-")
        plt.xticks(rotation=45, ha="right")
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
        get_plot(
            "avg_per_valuetype",
            "Temps moyen d'execution en fonction du type de valeurs",
            "Type de valeurs",
            "Temps",
        )


def run_bench_on_algorithm():
    results = []
    for size in array_sizes:
        for spread in spreads:
            for function in array_functions:
                res = bench_file(size, spread, function)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

    get_diagram(
        "total_par_algo",
        "Temps moyen par algorithme sur tous les benchmarks",
        "Algorithme",
        "Temps",
        avgs,
        files,
    )


### Début Programme Principal ###
files = search_algorithms()

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")
    exit()

str_array_functions = []
for i in range(len(array_functions)):
    s = str(array_functions[i])
    debut_nom = s.find(" ") + 1
    fin_nom = s.find(" at")
    s = s[debut_nom:fin_nom]
    str_array_functions.append(s)

run_bench_on_valuetype(files)
plt.clf()
run_bench_on_spreads(files)
plt.clf()
run_bench_on_arrsizes(files)
plt.clf()
run_bench_on_algorithm()


# avg_per_file = get_avg_per_file(results)
# get_diagram(
#     "results/total_par_algo",
#     "Temps moyen par algo sur tous les benchmarks",
#     "algo",
#     "temps",
#     avg_per_file,
#     files,
# )
# plt.clf()

# for i in range(len(files)):
#     avg_per_arrsize = get_avg_per_arrsize(results, array_sizes, i)
#     plt.plot(array_sizes, avg_per_arrsize, label=files[i])
#
# get_plot(
#     "results/total_par_arrsize",
#     "Temps moyen de chaque algorithme en fonction de la taille du tableau",
#     "Taille du tableau",
#     "Temps",
# )
# plt.clf()
#
# for i in range(len(files)):
#     avg_per_spread = get_avg_per_spread(results, spreads, i)
#     plt.plot(spreads, avg_per_spread, label=files[i])
#
# get_plot(
#     "results/total_par_spread",
#     "Temps moyen de chaque algorithme en fonction de la plage de données dans le tableau",
#     "Plage de données",
#     "Temps",
# )
# plt.clf()
#
# str_array_functions = []
# for i in range(len(array_functions)):
#     s = str(array_functions[i])
#     debut_nom = s.find(" ") + 1
#     fin_nom = s.find(" at")
#     s = s[debut_nom:fin_nom]
#     str_array_functions.append(s)
#
# all_avgs_per_valuetype = []  # liste de toutes les liste de avg per valuetype
# for i in range(len(files)):
#     all_avgs_per_valuetype.append(get_avg_per_valuetype(results, array_functions, i))
#
# for i in range(len(all_avgs_per_valuetype)):
#     get_diagram(
#         "results/total_per_valuetype_" + str(i),
#         "Temps moyen du " + files[i] + " en fonction du type de valeurs",
#         "Type de valeurs",
#         "Temps",
#         all_avgs_per_valuetype[i],
#         str_array_functions,
#     )
