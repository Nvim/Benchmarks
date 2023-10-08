#include "../include/lib.h"
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

// remplit un tableau de valeurs croissantes
int *fill_tab_asc(int *tab, int taille) {
  for (int i = 0; i < taille; i++) {
    tab[i] = i;
  }
  return tab;
}

// remplit un tableau de valeurs aléatoires
void initialisation_aleatoire(int *tab, int taille, int min, int max) {
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % (max - min + 1) + min;
  }
}

void copie_tableau(int *source, int *destination, int taille) {
  for (int i = 0; i < taille; i++) {
    destination[i] = source[i];
  }
}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void swap_float(float *a, float *b) {
  float temp = *a;
  *a = *b;
  *b = temp;
}

// // returns an array of all C files containing "sort" substring in their name
// file_node *get_sort_files() {
//   DIR *dir;
//   struct dirent *entry;
//   const char *path = ".";
//   dir = opendir(path);
//
//   if (dir == NULL) {
//     perror("Erreur lors de l'ouverture du dossier");
//     return NULL;
//   }
//
//   file_node *head = NULL;
//
//   // Parcourez les fichiers dans le dossier
//   while ((entry = readdir(dir)) != NULL) {
//     // Ignorer les entrées spéciales "." et ".."
//     if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0)
//     {
//       // Vérifiez si le nom du fichier contient le mot "sort"
//       if (strstr(entry->d_name, "sort") != NULL) {
//         file_node *node = createFileNameNode(entry->d_name);
//         if (node != NULL) {
//           if (head == NULL) {
//             head = node;
//           } else {
//             head = ajout_tete(head, node);
//           }
//         }
//       }
//     }
//   }
//
//   // Fermez le dossier
//   closedir(dir);
//   return head;
// }

void read_csv() {
  FILE *fp = fopen("arrays/array.csv", "r");

  if (fp == NULL) {
    fprintf(stderr, "*** Erreur lors de l'ouverture du fichier");
    return;
  }

  char ligne[1024]; // Stocker la ligne lue depuis le fichier
  // fgets(ligne, sizeof(ligne), fp);
  // int array_size = atoi(strtok(ligne, ","));
  // if (array_size < 1) {
  //   fprintf(stderr, "*** Erreur: taille du tableau invalide");
  //   return NULL;
  // }
  // int *tab = creation_tableau(array_size);
  int i = 0;

  while (fgets(ligne, sizeof(ligne), fp)) {
    // Utiliser strtok pour diviser la ligne en valeurs séparées par des
    // virgules
    char *token = strtok(ligne, ",");
    while (token != NULL) {
      // Convertir le token en un entier
      int entier = atoi(token);
      printf("%d", entier);
      // tab[i] = atoi(token);
      // Obtenir le prochain token
      token = strtok(NULL, ",");
    }
    printf("\n");
  }

  // Fermer le fichier
  fclose(fp);
  printf("fini");
  // return tab;
}

void run_test_verbose(int *tab, int taille, TriFunction tri_func) {

  printf("- Tableau initial: \n");
  affichage_tableau(tab, taille);
  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  clock_t debut = clock();
  tri_func(tab, taille);
  clock_t fin = clock();

  printf("- Tableau trié: \n");
  affichage_tableau(tab, taille);
  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);
}

void run_test(int *tab, int taille, TriFunction tri_func) {

  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  clock_t debut = clock();
  tri_func(tab, taille);
  clock_t fin = clock();

  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);
}
