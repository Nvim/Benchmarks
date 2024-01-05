import csv
import os
import random

from sympy import isprime


def write_csv(values_arr, array_dir):
    if not os.path.exists(array_dir):
        os.makedirs(array_dir)

    csv_file_path = os.path.join(array_dir, "test.csv")
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(values_arr)

    print(f"Le fichier CSV a été créé avec succès à l'emplacement : {csv_file_path}")


def random_values(array_size, min, max):
    random_values = [random.randint(min, max) for _ in range(array_size)]
    return random_values


# nombres pairs uniquement
def random_even_values(array_size, min, max):
    random_values = [
        random.randint(min // 2, (max // 2) + 1) * 2 for _ in range(array_size)
    ]
    return random_values


# nombres impairs uniquement
def random_uneven_values(array_size, min, max):
    random_values = [
        random.randint(min // 2, (max // 2) + 1) * 2 + 1 for _ in range(array_size)
    ]
    return random_values


# nombres premiers uniquement
def random_prime_values(array_size, min, max):
    random_values = []
    while len(random_values) < array_size:
        candidate = random.randint(min, max)
        if candidate % 2 == 0:
            continue

        if isprime(candidate):
            random_values.append(candidate)

    return random_values


# tableau trié dans le mauvais ordre
def worst_case(array_size, min, max):
    random_values = []
    for i in range(array_size, 0):
        random_values[i] = i
    return random_values
