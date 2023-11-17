import os
import fnmatch
import re
import subprocess

array_size = "15000"
nb_calls = 20

def search_algorithms():
    folder = 'lib'
    extension = '.so'
    files = []
    # Parcours du dossier
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, '*' + extension):
            filename = os.path.splitext(filename)[0][3:]
            files.append(filename)
    return files

# Début programme
files = search_algorithms()

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")


# Liste pour stocker les temps d'exécution
temps_execution = []

for i in range (len(files)):
    for _ in range(nb_calls):
        cmd = ["bin/main", files[i], str(array_size)]
        sortie = subprocess.check_output(cmd, shell=False)
        temps_match = re.search(r"Temps d'exécution : (\d+\.\d+) secondes", sortie.decode("utf-8"))
        if temps_match:
            temps_execution.append(float(temps_match.group(1)))
        else:
            print("Erreur : impossible de trouver le temps d'éxécution dans la sortie.")

        avg = 0.0
        for j in temps_execution:
            avg += j
        
    avg = avg/len(temps_execution)
    print("Average "+ files[i] + ": " f"{avg} secs")


# Affiche les temps d'exécution
# print("Temps d'éxécution pour chaque appel :")
# for temps in temps_execution:
#     print(f"{temps} secondes")


