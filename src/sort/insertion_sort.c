void insertion_sort(int *tab, int taille) {
  int i, key, j;
  for (i = 1; i < taille; i++) {
    key = tab[i];
    j = i - 1;

    while (j >= 0 && tab[j] > key) {
      tab[j + 1] = tab[j];
      j = j - 1;
    }
    tab[j + 1] = key;
  }
}
