#include "../../include/lib.h"

int getNextGap(int gap)
{
    // Shrink gap by Shrink factor
    gap = (gap*10)/13;
 
    if (gap < 1)
        return 1;
    return gap;
}
 
// Function to sort a[0..n-1] using Comb Sort
void comb_sort(int *tab, int taille)
{
    // Initialize gap
    int gap = taille;
 
    // Initialize swapped as true to make sure that
    // loop runs
    uint_fast8_t swapped = 1;
 
    // Keep running while gap is more than 1 and last
    // iteration caused a swap
    while (gap != 1 || swapped == 1)
    {
        // Find next gap
        gap = getNextGap(gap);
 
        // Initialize swapped as false so that we can
        // check if swap happened or not
        swapped = 0;
 
        // Compare all elements with current gap
        for (int i=0; i<taille-gap; i++)
        {
            if (tab[i] > tab[i+gap])
            {
                swap(&tab[i], &tab[i+gap]);
                swapped = 1;
            }
        }
    }
}
