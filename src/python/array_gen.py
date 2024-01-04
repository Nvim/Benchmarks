import csv
import os
import random


def random_values(array_size, array_dir, min, max):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = [random.randint(min, max) for _ in range(array_size)]

    # Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, "test.csv")

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)

    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")


# nombres pairs uniquement
def random_even_values(array_size, array_dir, min, max):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = [
        random.randint(min // 2, (max // 2) + 1) * 2 for _ in range(array_size)
    ]

    # Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, "test.csv")

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)
    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")


# nombres impairs uniquement
def random_uneven_values(array_size, array_dir, min, max):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = [
        random.randint(min // 2, (max // 2) + 1) * 2 + 1 for _ in range(array_size)
    ]

    # Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, "test.csv")

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)
    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")


# nombres premiers uniquement
def random_prime_values(array_size, array_dir, min, max):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = [random.randint(min, max) for _ in range(array_size)]

    # Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, "test.csv")

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)

    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")


# tableau trié dans le mauvais ordre
def worst_case(array_size, array_dir, min, max):
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    # Générer des valeurs aléatoires
    random_values = []
    for i in range(array_size, 0):
        random_values[i] = i

    # Chemin complet du fichier CSV
    csv_file_path = os.path.join(array_dir, "test.csv")

    # Écrire les valeurs dans le fichier CSV
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Écrire toutes les valeurs sur une seule ligne séparées par des virgules
        csv_writer.writerow(random_values)

    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")
