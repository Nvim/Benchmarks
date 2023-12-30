#include "../../include/lib.h"

typedef struct Tree {
  int value;
  struct Tree *left, *right;
} Tree;

Tree *new_tree(int value) {
  Tree *tmp = (Tree *)malloc(sizeof(Tree));
  tmp->value = value;
  tmp->left = tmp->right = NULL;

  return tmp;
}

// chaque élément de l'arbre est unique
Tree *insert(Tree *tree, int value) {
  if (tree == NULL) {
    return new_tree(value);
  }
  if (value > tree->value) {
    tree->right = insert(tree->right, value);
  } else if (value < tree->value) {
    tree->left = insert(tree->left, value);
  }
  return tree;
}

// stocke les valeurs de l'arbre dans un tableau
void store_sorted(Tree *root, int *arr, int i) {
  if (root != NULL) {
    store_sorted(root->left, arr, i);
    arr[i] = root->value;
    i++;
    store_sorted(root->right, arr, i);
  }
}

int *tree_sort(int *tab, int taille) {
  Tree *root = NULL;

  // Construct the BST
  root = insert(root, tab[0]);
  for (int i = 1; i < taille; i++)
    root = insert(root, tab[i]);

  // Store inorder traversal of the BST
  // in arr[]
  int i = 0;
  store_sorted(root, tab, i);
  return tab;
}
