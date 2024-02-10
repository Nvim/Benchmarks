import fnmatch
import os
import re
import subprocess
import sys
from datetime import datetime
from typing import List

import array_gen
import matplotlib.pyplot as plt
import numpy as np

now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
array_dir = "arrays"
graph_dir = "graphs_" + now
graph_ext = ".png"

nb_calls = 3
array_sizes = [10, 100, 1000, 10000, 20000, 50000]
spreads = [10, 100, 1000, 100000, 1000000]
min_value = 0
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


def search_algorithms(name):
    folder = "lib"
    extension = ".so"
    files = []
    # Parcours du dossier
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, name + extension):
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


# temps exec moyen de chaque algo sur les critères spécifiés
def test_all_files(array_size, spread, array_function):
    temps_execution = []
    for i in range(len(files)):
        tmp_temps_execution = []
        arr = array_function(array_size, min_value, spread)
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


# temps d'exec moyen de chaque array_sizes, avec les critères spécifiés
def test_arrsize(algorithm, spread, array_function):
    temps_execution = []
    for i in range(len(array_sizes)):
        tmp_temps_execution = []
        arr = array_function(array_sizes[i], min_value, spread)
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


# temps d'exec moyen de chaque spread, avec les critères spécifiés
def test_spread(algorithm, array_size, array_function):
    temps_execution = []
    for i in range(len(spreads)):
        tmp_temps_execution = []
        arr = array_function(array_size, min_value, spreads[i])
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


# temps d'exec moyen de chaque nature de données, avec les critères spécifiés
def test_array_func(algorithm, array_size, spread):
    temps_execution = []
    for i in range(len(array_functions)):
        tmp_temps_execution = []
        arr_func = array_functions[i]
        arr = arr_func(array_size, min_value, spread)
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


def run_bench_on_arrsizes(files, individual=0):
    prefix = ""
    sufix = ""
    if individual == 1:
        prefix = "individual/"
        sufix = "_" + files[0]
    for file in files:
        results = []
        for spread in spreads:
            for array_func in array_functions:
                res = test_arrsize(file, spread, array_func)
                results.append(res)

        avgs = [0] * len(results[0])
        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        avgs = [avg / len(results) for avg in avgs]
        plt.plot(array_sizes, avgs, label=file)
        get_plot(
            prefix + "avg_per_arrsize" + sufix,
            "Temps moyen d'execution en fonction de la taille du tableau.\n (nb_calls: "
            + str(nb_calls)
            + ", min_value: "
            + str(min_value)
            + ")",
            "Taille Tableau",
            "Temps",
        )


def run_bench_on_spreads(files, individual=0):
    prefix = ""
    sufix = ""
    if individual == 1:
        prefix = "individual/"
        sufix = "_" + files[0]
    results = []
    for file in files:
        for size in array_sizes:
            for function in array_functions:
                res = test_spread(file, size, function)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        avgs = [avg / len(results) for avg in avgs]
        plt.plot(spreads, avgs, label=file)
        get_plot(
            prefix + "avg_per_spread" + sufix,
            "Temps moyen d'execution en fonction de la fourchette de valeurs \n(nb_calls: "
            + str(nb_calls)
            + ", min_value: "
            + str(min_value)
            + ")",
            "Fourchette",
            "Temps",
        )


def run_bench_on_valuetype(files, individual=0):
    prefix = ""
    sufix = ""
    if individual == 1:
        prefix = "individual/"
        sufix = "_" + files[0]
    results = []
    for file in files:
        for size in array_sizes:
            for spread in spreads:
                res = test_array_func(file, size, spread)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

        plt.plot(str_array_functions, avgs, label=file, marker="o", linestyle="-")
        plt.xticks(rotation=45, ha="right")
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
        get_plot(
            prefix + "avg_per_datatype" + sufix,
            "Temps moyen d'execution en fonction du type de valeurs\n (nb_calls: "
            + str(nb_calls)
            + ", min_value: "
            + str(min_value)
            + ")",
            "Type de valeurs",
            "Temps",
        )


def run_bench_on_all_algorithms():
    results = []
    for size in array_sizes:
        for spread in spreads:
            for function in array_functions:
                res = test_all_files(size, spread, function)
                results.append(res)

        avgs = [0] * len(results[0])

        for tab in results:
            for i, valeur in enumerate(tab):
                avgs[i] += valeur

    get_diagram(
        "avg_per_algorithm",
        "Temps moyen par algorithme sur tous les benchmarks\n (nb_calls: "
        + str(nb_calls)
        + ", min_value: "
        + str(min_value)
        + ")",
        "Algorithme",
        "Temps",
        avgs,
        files,
    )


### Début Programme Principal ###
if not os.path.exists(graph_dir):
    os.makedirs(graph_dir)

args = sys.argv[1:]
files = []
if args:
    for arg in args:
        arg = "lib" + arg
        files.append(search_algorithms(arg)[0])
else:
    files = search_algorithms("*")

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")
    exit()

if not os.path.exists(graph_dir + "/individual"):
    os.makedirs(graph_dir + "/individual")

str_array_functions = []
for i in range(len(array_functions)):
    s = str(array_functions[i])
    debut_nom = s.find(" ") + 1
    fin_nom = s.find(" at")
    s = s[debut_nom:fin_nom]
    str_array_functions.append(s)

print("*** Début du programme ***")
print("\n")
print("ça peut être long (vraiment)")
print("\n")
# print("* Lancement des tests individuels...")
#
# ### BENCHMARKS INDIVIDUELS ###
# for i in range(len(files)):
#     tmp_files = []
#     tmp_files.append(files[i])
#     run_bench_on_valuetype(tmp_files, 1)
#     plt.clf()
#     run_bench_on_spreads(tmp_files, 1)
#     plt.clf()
#     run_bench_on_arrsizes(tmp_files, 1)
#     plt.clf()
#
run_bench_on_all_algorithms()
plt.clf()
# # Si il n'y a qu'un algo, pas besoin des benchs globaux
# if len(files) == 1:
#     exit()

print("Lancement des tests globaux...")
### BENCHMARKS GLOBAUX ###
run_bench_on_valuetype(files)
plt.clf()
run_bench_on_spreads(files)
plt.clf()
run_bench_on_arrsizes(files)
plt.clf()
