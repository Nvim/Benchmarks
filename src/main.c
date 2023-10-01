#include "../include/lib.h"
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{

  const char *function_name;
  TriFunction function;
  char libname[256];
  void *lib_handle;

  if(argc <= 1){
    fprintf(stderr, "\n**ERREUR: Aucune fonction de tri specifiee. **\n");
    return EXIT_FAILURE;
  }

  function_name = argv[1];
  snprintf(libname, sizeof(libname), "lib/lib%s.so", function_name);

  lib_handle = dlopen(libname, RTLD_LAZY);
  if(!lib_handle){
    fprintf(stderr, "\nERREUR: impossible de charger la bibliotheque %s\n", dlerror());
    return EXIT_FAILURE;
  }

  function = (TriFunction)dlsym(lib_handle, function_name);
  if(!function){
    fprintf(stderr, "\nERREUR: fonction de tri introuvable dans la bibliotheque %s\n", dlerror());
    dlclose(lib_handle);
    return EXIT_FAILURE;
  }


  srand(time(NULL));

  int * tab = creation_tableau(TAILLE);
  initialisation_aleatoire(tab, TAILLE, 0, 2000);


  run_test_verbose(tab, TAILLE, function);

  free(tab);
  tab = NULL;
  dlclose(lib_handle);

  return EXIT_SUCCESS;
}
