#include "../include/lib.h"

int is_sorted(int *tab, int taille){
  for(int i = 0; i<taille-1; i++){
    if(tab[i] > tab[i+1]){
      return 0;
    }
  }
  return 1;
}

void affichage_tableau(int *tab, int taille) {
  for (int i = 0; i < taille; i++) {
    printf("%d, ", tab[i]);
  }
  printf("\n");
}

// alloue un tableau vide de taille taille et le retourne
int * creation_tableau(int taille) {
  int *tab = malloc(sizeof(int) * taille);
  return tab;
}

// remplit un tableau de valeurs croissantes
int *fill_tab_asc(int *tab, int taille) {
  for (int i = 0; i < taille; i++) {
    tab[i] = i;
  }
  return tab;
}

// remplit un tableau de valeurs aléatoires
void initialisation_aleatoire(int *tab, int taille, int min, int max) {
  for (int i = 0; i < taille; i++) {
    tab[i] = rand() % (max - min + 1) + min;
  }
}

void copie_tableau(int *source, int *destination, int taille){
  for(int i = 0; i < taille; i++){
    destination[i] = source[i];
  }
}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void swap_float(float *a, float *b) {
  float temp = *a;
  *a = *b;
  *b = temp;
}

void run_test_verbose(int * tab, int taille, TriFunction tri_func) {


  printf("- Tableau initial: \n");
  affichage_tableau(tab, taille);
  printf("- Tableau trié? %d\n", is_sorted(tab, taille));

  clock_t debut = clock();
  tri_func(tab, taille);
  clock_t fin = clock();

  printf("- Tableau trié: \n");
  affichage_tableau(tab, taille);
  printf("- Tableau trié? %d\n", is_sorted(tab, taille));


  double temps = (double)(fin-debut)/CLOCKS_PER_SEC;
  printf("Temps d'exécution : %f secondes\n", temps);

}
