#include "../../include/lib.h"

void merge(int tab[], int l, int m, int r) {
  int i, j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  // Create temp arrays
  int L[n1], R[n2];

  // Copy data to temp arrays L[] and R[]
  for (i = 0; i < n1; i++)
    L[i] = tab[l + i];
  for (j = 0; j < n2; j++)
    R[j] = tab[m + 1 + j];

  // Merge the temp arrays back into arr[l..r
  i = 0;
  j = 0;
  k = l;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      tab[k] = L[i];
      i++;
    } else {
      tab[k] = R[j];
      j++;
    }
    k++;
  }

  // Copy the remaining elements of L[],
  // if there are any
  while (i < n1) {
    tab[k] = L[i];
    i++;
    k++;
  }

  // Copy the remaining elements of R[],
  // if there are any
  while (j < n2) {
    tab[k] = R[j];
    j++;
    k++;
  }
}

void merge_sort(int *tab, int debut, int fin) {
  if (debut < fin) {
    int m = debut + (fin - debut) / 2;

    // Sort first and second halves
    merge_sort(tab, debut, m);
    merge_sort(tab, m + 1, fin);

    merge(tab, debut, m, fin);
  }
}
