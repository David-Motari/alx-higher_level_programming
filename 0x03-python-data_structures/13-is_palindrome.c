#include "lists.h"

/**
* reverse_listint - reverses a singly linke list.
* @head: pointer to head node.
*
* Return: pointer to head of reversed list.
*/

listint_t *reverse_listint(listint_t **head)
{
listint_t *node = *head, *next, *prev = NULL;

while (node != NULL)
{
	next = node->next;
	node->next = prev;
	prev = node;
	node = next;
}
*head = prev;
return (*head);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: pointer to head node.
*
* Return: 1 if palidrome or 0 if not palidrome.
*/

int is_palindrome(listint_t **head)
{
listint_t *trav, *rv, *md;
size_t size = 0, i;

if (*head == NULL || (*head)->next == NULL)
	return (1);
trav = *head;
while (trav)
{
	size++;
	trav = trav->next;
}
trav = *head;
for (i = 0; i < (size/2) - 1; i++)
	trav = trav->next;

if ((size % 2) == 0 && trav->n != trav->next->n)
	return (0);

trav = trav->next->next;
rv = reverse_listint(&trav);
md = rv;

trav = *head;
while (rv)
{
if (trav->n != rv->n)
	return (0);
trav = trav->next;
rv = rv->next;
}
reverse_listint(&md);

return (1);
}

