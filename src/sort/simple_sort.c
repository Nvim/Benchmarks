#include "../../include/lib.h"

void simple_sort(int * tab, int taille){
  int i, j, min_index;
  for (i = 0; i < taille - 1; i++) {
    // Trouver l'indice du minimum dans la partie non triée
    min_index = i;
    for (j = i + 1; j < taille; j++) {
      if (tab[j] < tab[min_index]) {
        min_index = j;
      }
    }
    // Échanger l'élément minimum avec l'élément à la position i
    swap(&tab[i], &tab[min_index]);
  }
}
