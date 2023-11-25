#include "../include/lib.h"
#include <stdint.h>
#include <stdio.h>
#include <string.h>

int is_sorted(int *tab, int taille) {
  for (int i = 0; i < taille - 1; i++) {
    if (tab[i] > tab[i + 1]) {
      return 0;
    }
  }
  return 1;
}

void affichage_tableau(int *tab, int taille) {
  for (int i = 0; i < taille; i++) {
    printf("%d, ", tab[i]);
  }
  printf("\n");
}

// alloue un tableau vide de taille taille et le retourne
int *creation_tableau(int taille) {
  int *tab = malloc(sizeof(int) * taille);
  return tab;
}

// remplit un tableau de valeurs aléatoires
void initialisation_aleatoire(int *tab, int taille, int min, int max) {
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % (max - min + 1) + min;
  }
}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void random_tab(int size) {
  FILE * fp = fopen("arrays/array.csv", "w");
  for (int i = 0; i < size; i++) {
    fprintf(fp, "%d,", rand() % 10000);
  }
  fclose(fp);
}

int *read_csv(int array_size) {
  FILE *fp = fopen("arrays/test.csv", "r");

  if (fp == NULL) {
    fprintf(stderr, "*** Erreur lors de l'ouverture du fichier");
    return NULL;
  }

  char ligne[MAX_LINE_LENGTH]; // Stocker la ligne lue depuis le fichier
  int *tab = creation_tableau(array_size);

  int i = 0;

  while (fgets(ligne, sizeof(ligne), fp)) {
    // Utiliser strtok pour diviser la ligne en valeurs séparées par des
    // virgules
    char *token = strtok(ligne, ",");
    while (token != NULL) {
      // Convertir le token en un entier
      int entier = atoi(token);
      tab[i] = atoi(token);
      // Obtenir le prochain token
      token = strtok(NULL, ",");
      i++;
    }
  }

  // Fermer le fichier
  fclose(fp);
  printf("\nLecture du fichier terminée.\n");
  return tab;
}

void run_test_verbose(int *tab, int taille, SortFunction tri_func) {

  printf("\t-- Tableau initial --\n");
  affichage_tableau(tab, taille);
  printf("-> Tableau trié? %d\n", is_sorted(tab, taille));

  clock_t debut = clock();
  tri_func(tab, taille);
  clock_t fin = clock();

  printf("\n\t-- Tableau trié: --\n");
  affichage_tableau(tab, taille);
  printf("-> Tableau trié? %d\n", is_sorted(tab, taille));

  double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);
}

void run_test(int *tab, int taille, SortFunction tri_func) {

  printf("- Tableau trié? %d, (Taille: %d)\n", is_sorted(tab, taille), taille);

  clock_t debut = clock();
  tri_func(tab, taille);
  clock_t fin = clock();

  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);
}

void run_test_merge(int *tab, int taille, int debut, int fin, MergeFunction tri_func) {

  printf("- Tableau trié? %d, (Taille: %d)\n", is_sorted(tab, taille), taille);

  clock_t debut_temps = clock();
  tri_func(tab, debut, fin);
  clock_t fin_temps = clock();

  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  double temps = (double)(fin_temps - debut_temps) / CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);
}
