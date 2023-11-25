import csv
import os
import random

def random_values(array_size, array_dir):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = [random.randint(1, 1000) for _ in range(1999)]

# Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, 'test.csv')

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)

    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")
