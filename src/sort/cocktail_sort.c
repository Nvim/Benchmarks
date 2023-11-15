#include "../../include/lib.h"
#include <stdint.h>
#include <stdio.h>

// Fonction pour implémenter le tri cocktail
void cocktail_sort(int *tab, int taille) {
  uint_fast8_t swapped = 1; // Variable pour vérifier s'il y a eu un échange
  int start = 0, end = taille - 1;
  int i;

  while (swapped) {

    swapped = 0;
    for (i = start; i < end; ++i) {
      if (tab[i] > tab[i + 1]) {
        swap(&tab[i], &tab[i + 1]);
        swapped = 1;
      }
    }

    if (!swapped) {
      break;
    }
    swapped = 0;
    --end;

    for (i = end-1; i >= start; --i) {
      if (tab[i] > tab[i + 1]) {
        swap(&tab[i], &tab[i + 1]);
        swapped = 1;
      }
    }
    ++start;
  }
}
