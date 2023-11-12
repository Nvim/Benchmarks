import os
import fnmatch

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

if fnmatch.fnmatch('config', '*' + '.json'):
    print("Fichier de configuration trouvé!")
else:
    print("Erreur: Aucune configuration trouvée.")

if not files:
    print("Erreur: Aucun algorithme de tri trouvé")

print("Algorithmes disponibles:")
for file in files:
    print("* ", file)
