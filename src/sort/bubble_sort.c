#include "../../include/lib.h"

void bubble_sort(int * tab, int taille){
  int i, j;
  for (i = 0; i < taille - 1; i++) {
    for (j = 0; j < taille - 1; j++) {
      if (tab[j] > tab[j + 1]) {
        swap(&tab[j], &tab[j + 1]);
        // int temp = tab[j];
        // tab[j] = tab[j+1];
        // tab[j+1] = temp;
      }
    }
  }
}

// void bubble_sort_float(float *tab, int taille){
//   int i, j;
//   for (i = 0; i < taille - 1; i++) {
//     for (j = 0; j < taille - i - 1; j++) {
//       if (tab[j] > tab[j + 1]) {
//         swap_float(&tab[j], &tab[j + 1]);
//       }
//     }
//   }
// }
