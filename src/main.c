#include "../include/lib.h"
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[])
{

  srand(time(NULL));
  const char *function_name;
  char libname[256];
  void *lib_handle;
  void *function;
  uint8_t merge = 0;

  if(argc <= 2){
    fprintf(stderr, "\n**Usage: main <algorithm> <array_size>**\n");
    return EXIT_FAILURE;
  }
  function_name = argv[1];
  const int array_size = atoi(argv[2]);

  if(array_size < 1){
    fprintf(stderr, "\nERREUR: Taille de tableau invalide!\n");
    return EXIT_FAILURE;
  }
  printf("\nArray Size: %d", array_size);
  random_tab(array_size);

  int * array = read_csv(array_size);
  printf("\nLecture tableau réussie\n");


  snprintf(libname, sizeof(libname), "lib/lib%s.so", function_name);
  lib_handle = dlopen(libname, RTLD_LAZY);
  if(!lib_handle){
    fprintf(stderr, "\nERREUR: impossible de charger la bibliotheque %s\n", dlerror());
    return EXIT_FAILURE;
  }

  if(strcmp(function_name, "merge_sort") == 0){
    merge = 1;
    function = (MergeFunction*)dlsym(lib_handle, function_name);
  }
  else{
    function = (SortFunction*)dlsym(lib_handle, function_name);
  }
  if(!function){
    fprintf(stderr, "\nERREUR: fonction de tri introuvable dans la bibliotheque %s\n", dlerror());
    dlclose(lib_handle);
    return EXIT_FAILURE;
  }

  if(merge){
    run_test_merge(array, array_size, 0, array_size-1, function);
  }
  else{
    run_test_verbose(array, array_size, function);
  }

  free(array);
  array = NULL;
  dlclose(lib_handle);

  return EXIT_SUCCESS;
}
