#include "../../include/lib.h"

void bubble_sort_opt(int * tab, int taille){
  int i, j;
  for (i = 0; i < taille - 1; i++) {
    for (j = 0; j < taille - 1 - i; j++) {
      if (tab[j] > tab[j + 1]) {
        swap(&tab[j], &tab[j + 1]);
      }
    }
  }
}
