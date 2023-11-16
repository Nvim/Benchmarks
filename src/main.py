import os
import fnmatch
import re
import subprocess

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

# Exécute le programme C dix fois
for _ in range(10):
    sortie = subprocess.check_output("bin/main bubble_sort 2000", shell=True)

    # Utilise une expression régulière pour extraire le temps d'exécution de la dernière ligne
    temps_match = re.search(r"Temps d'exécution: (\d+\.\d+) secondes", sortie.decode("utf-8"))

    # Vérifie si la correspondance a été trouvée
    if temps_match:
        temps_execution.append(float(temps_match.group(1)))
    else:
        print("Erreur : impossible de trouver le temps d'éxécution dans la sortie.")

# Affiche les temps d'exécution
print("Temps d'éxécution pour chaque appel :")
for temps in temps_execution:
    print(f"{temps} secondes")
