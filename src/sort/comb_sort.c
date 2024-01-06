#include "../../include/lib.h"

int getNextGap(int gap) {
  // Shrink gap by Shrink factor
  gap = (gap * 10) / 13;

  if (gap < 1)
    return 1;
  return gap;
}

void comb_sort(int *tab, int taille) {
  int gap = taille;

  uint_fast8_t swapped = 1;

  while (gap != 1 || swapped == 1) {
    gap = getNextGap(gap);
    swapped = 0;

    for (int i = 0; i < taille - gap; i++) {
      if (tab[i] > tab[i + gap]) {
        swap(&tab[i], &tab[i + gap]);
        swapped = 1;
      }
    }
  }
}
