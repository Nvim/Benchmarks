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

  if(argc <= 2){
    fprintf(stderr, "\n**Usage: main.c <algorithm> <array_size>**\n");
    return EXIT_FAILURE;
  }

  int array_size;
  array_size = atoi(argv[2]);
  printf("\n%d\n", array_size);

  read_csv();
  // affichage_tableau(tab, sizeof(&tab)/sizeof(int));
  return 0;

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

  int * tab = creation_tableau(array_size);
  initialisation_aleatoire(tab, array_size, 0, 2000);


  run_test_verbose(tab, array_size, function);

  free(tab);
  tab = NULL;
  dlclose(lib_handle);

  return EXIT_SUCCESS;
}
