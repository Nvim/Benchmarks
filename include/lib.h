#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <dirent.h>
#include <dlfcn.h>

#define TAILLE 15
typedef void (*TriFunction)(int *, int);

typedef struct tree{
  int data;
  struct tree *right;
  struct tree *left;
} tree;

/*********************************************
 *            --- UTIL.C ---
 ********************************************/

int is_sorted(int *tab, int taille);

void affichage_tableau(int *tab, int taille);

// alloue un tableau vide de taille taille et le retourne
int *creation_tableau(int taille);

// remplit un tableau de valeurs croissantes
int *fill_tab_asc(int *tab, int taille);

// remplit un tableau de valeurs aléatoires
void initialisation_aleatoire(int *tab, int taille, int min, int max);

void copie_tableau(int *source, int *destination, int taille);

void swap(int *a, int *b);

void swap_float(float *a, float *b);

int check_args(char *arg);

void run_test_verbose(int *tab, int taille, TriFunction tri_func);

void run_test(int *tab, int taille, TriFunction tri_func);


/*********************************************
 *            --- FILE_NODE ---
 ********************************************/

file_node *createFileNameNode(const char *name);

void freeFileNameList(file_node *head);

file_node *ajout_tete(file_node *l, file_node *m);

void affichage_liste(file_node *l);
/*********************************************
 *            --- Sort Functions ---
 ********************************************/

void bubble_sort(int *tab, int taille);

void bubble_sort_float(float *tab, int taille);

void bubble_sort_opt(int *tab, int taille);

void simple_sort(int *tab, int taille);
