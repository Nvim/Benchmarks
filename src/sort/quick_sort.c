#include "../../include/lib.h"

int partition(int *tab, int low, int high) {
  int pivot = tab[high];
  int i = (low - 1);

  for (int j = low; j <= high - 1; j++) {
    if (tab[j] <= pivot) {
      i++;
      swap(&tab[i], &tab[j]);
    }
  }
  swap(&tab[i + 1], &tab[high]);
  return (i + 1);
}

void quick_sort(int *tab, int low, int high) {
  if (low < high) {
    int pi = partition(tab, low, high);

    quick_sort(tab, low, pi - 1);
    quick_sort(tab, pi + 1, high);
  }
}
