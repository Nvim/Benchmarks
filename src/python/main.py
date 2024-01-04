import fnmatch
import os
import re
import subprocess

import random_big_values
import random_small_values

nb_calls = 20
array_size = 15000
array_dir = "arrays"


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


def benchmark(files, array_function):
    array_function(array_size, array_dir)
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


# Début programme
files = search_algorithms()

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")

# Liste pour stocker les temps d'exécution
temps_execution = []
temps_execution = benchmark(files, random_small_values.random_small_values)

for i in range(len(temps_execution)):
    print("Average " + files[i] + ": " f"{temps_execution[i]} secs.")
