#include <dirent.h>
#include <dlfcn.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

#define TAILLE 15
#define MAX_LINE_LENGTH 32768
typedef void (*SortFunction)(int *, int);
typedef void (*MergeFunction)(int *, int, int);

// typedef struct file_node{
//   char * name;
//   struct file_node * next;
// } file_node;

typedef struct tree {
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

void croissant(int *tab, int taille, uint_fast8_t *swapped);

void decroissant(int *tab, int taille, uint_fast8_t *swapped);

void random_tab(int size);

int check_args(char *arg);

int *read_csv(int array_size);

void run_test_verbose(int *tab, int taille, SortFunction tri_func);

void run_test(int *tab, int taille, SortFunction tri_func);

void run_test_merge(int *tab, int taille, int debut, int fin, MergeFunction tri_func);

/*********************************************
 *            --- FILE_NODE ---
 ********************************************/

// file_node *createFileNameNode(const char *name);
//
// void freeFileNameList(file_node *head);
//
// file_node *ajout_tete(file_node *l, file_node *m);
//
// void affichage_liste(file_node *l);
/*********************************************
 *            --- Sort Functions ---
 ********************************************/

void bubble_sort(int *tab, int taille);

void bubble_sort_float(float *tab, int taille);

void bubble_sort_opt(int *tab, int taille);

void simple_sort(int *tab, int taille);
