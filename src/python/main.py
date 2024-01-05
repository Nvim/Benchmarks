import fnmatch
import os
import re
import subprocess

import array_gen
import matplotlib.pyplot as plt

nb_calls = 20
array_size = 15000
array_dir = "arrays"

MAX_32_BIT = 2147483645
MIN_32_BIT = -2147483645


def search_algorithms():
    folder = "lib"
    extension = ".so"
    files = []
    # Parcours du dossier
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, "*" + extension):
            filename = os.path.splitext(filename)[0][3:]
            files.append(filename)
    return files


def get_diagram(filename, title, xlabel, ylabel, xdata, ydata):
    plt.bar(ydata, xdata, color="blue", width=0.7, bottom=0)
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)


# retourne le temps d'éxécution moyen de chaque algo dans une liste
def benchmark(files, array_function, min, max):
    array_gen.write_csv(array_function(array_size, min, max), array_dir)
    tmp_temps_execution = []
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


### Début Programme Principal ###
files = search_algorithms()

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")
    exit()

# Liste pour stocker les temps d'exécution
temps_execution = []
temps_execution = benchmark(files, array_gen.worst_case, 10, 10)
get_diagram(
    "prime.png",
    "Pire cas possible",
    "Algorithme",
    "Temps moyen (ms)",
    temps_execution,
    files,
)
