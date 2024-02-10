#include "../../include/lib.h"

void counting_sort(int *tab, int taille) {

  int max = tab[0];
  int i;
  for (i = 1; i < taille; i++) {
    if (tab[i] > max) {
      max = tab[i];
    }
  }

  int count[max + 1];
  for (i = 0; i <= max; i++) {
    count[i] = 0;
  }

  for (i = 0; i < taille; i++) {
    count[tab[i]]++;
  }

  int index = 0;
  for (i = 0; i <= max; i++) {
    while (count[i] > 0) {
      tab[index++] = i;
      count[i]--;
    }
  }
}
