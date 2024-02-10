# Projet algorithmie L3 MIAGE

## Benchmarks d'algorithmes de tri

### Description

Le projet est composé d'un programme C et d'un programme Python.

- Le programme C éxécute un algorithme de tri dont le nom est passé en argument sur un tableau lu dans un fichier CSV,
  et retourne le temps d'éxécution.

- Le programme Python génère les fichiers CSV contenant les tableaux en fonction de plusieurs critères (taille, fourchette de
  données, type de valeurs, ...) et invoque le programme C un certain nombre de fois pour chaque algorithme séléctionné.

- Le programme Python génère des graphiques de performance des algorithmes pour chaque benchmark effectué dans un nouveau
  dossier avec un nom unique.

### Algorithmes

**10 algorithmes sont disponibles, ils ont tous été implémentés en C.**

- Bubble Sort
- Bubble Sort Optimisé
- Cocktail Sort
- Comb Sort
- Counting Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Selection Sort
- Tree Sort

### Utilisation du projet

```
make

src/Python/main.py
```

Pour choisir quels algorithmes tester, passer les noms en argument au programme.
Si aucun argument spécifié, un benchmark se lance sur les 10 algorithmes disponibles.

- Plus de détails sur comment paramétrer le benchmark sont disponibles dans le **Rapport PDF**.
