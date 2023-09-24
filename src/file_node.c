#include "../include/lib.h"

// Fonction pour créer un nouveau nœud de nom de fichier
file_node *createFileNameNode(const char *name) {
  file_node *node = (file_node *)malloc(sizeof(file_node));
  if (node != NULL) {
    node->name =
        strdup(name); // Dupliquer le nom pour éviter des problèmes de mémoire
    node->next = NULL;
  }
  return node;
}

void freeFileNameList(file_node *head) {
  file_node *current = head;
  while (current != NULL) {
    file_node *temp = current;
    current = current->next;
    free(temp->name); // Libérer la mémoire du nom
    free(temp);       // Libérer la mémoire du nœud
  }
}

void affichage_liste(file_node *l)
{
    while (l != NULL)
    {
        printf("%s->", l->name);
        l = l->next;
    }
    printf("NULL");
}

// ajoute un element en tete (tete = premier element de la liste):
file_node *ajout_tete(file_node *l, file_node *m)
{
    if (m == NULL)
    {
        return l;
    }
    if (l == NULL)
        return m;
    if (m->next == NULL)
    {
        m->next = l;
    }
    else
    {
        file_node *tmp = m;
        while (tmp->next != NULL)
        {
            tmp = tmp->next;
        }
        tmp->next = l;
    }
    return m;
}
