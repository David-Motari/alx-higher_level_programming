#include "lists.h"
#include <stdlib.h>
/**
*insert_node - inserts a number into a sorted singly linked list
*@head: address of the address of the first node in thr list
*@number: value of the new node
*
*Return: address of the new node, else NULL 
*/ 

listint_t *insert_node(listint_t **head, int number)
{

listint_t *new, *current, *prev;
	
if (head == NULL)
return (NULL);

/*Create new node*/

new = malloc(sizeof(listint_t));

if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;

/*new node at the begining*/

if (*head == NULL || (*head)->n > number)
{

new->next = *head;
*head = new;
return (new);

}
/*add new node at correct position*/
prev = *head;
current = *head;

while (current)
{

if (current->n > number)
{
break;
}

prev = current;
current = current->next;

}
/*node at the end of the list*/

prev->next = new;
new->next = current;

return (new);
}
