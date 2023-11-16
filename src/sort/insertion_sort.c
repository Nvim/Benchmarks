/* Function to sort an array using insertion sort*/
void insertion_sort(int *tab, int taille)
{
    int i, key, j;
    for (i = 1; i < taille; i++) {
        key = tab[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
        while (j >= 0 && tab[j] > key) {
            tab[j + 1] = tab[j];
            j = j - 1;
        }
        tab[j + 1] = key;
    }
}
