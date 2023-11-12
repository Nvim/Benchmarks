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
    fprintf(stderr, "\n**Usage: main <algorithm> <array_size>**\n");
    return EXIT_FAILURE;
  }

  int array_size;
  array_size = atoi(argv[2]);
  if(array_size < 1){
    fprintf(stderr, "\nERREUR: Taille de tableau invalide!\n");
    return EXIT_FAILURE;
  }
  printf("\nArray Size: %d\n", array_size);

  int * array = read_csv(array_size);
  printf("\n");

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

  run_test_verbose(array, array_size, function);

  free(array);
  array = NULL;
  dlclose(lib_handle);

  return EXIT_SUCCESS;
}
