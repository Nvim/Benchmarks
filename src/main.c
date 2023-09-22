#include "../include/lib.h"
#include <time.h>

int main(int argc, char *argv[])
{
  int taille = 15;

  srand(time(NULL));

  int * tab = creation_tableau(taille);
  initialisation_aleatoire(tab, taille, 0, 20);

  TriFunction function = simple_sort;

  run_test_verbose(tab, taille, function);

  free(tab);
  tab = NULL;

  return EXIT_SUCCESS;
}
