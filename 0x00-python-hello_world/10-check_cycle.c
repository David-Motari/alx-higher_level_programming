#include "lists.h"

/**
* check_cycle - Using Floyd's Cycle-Finding Algorithm to check for cycle
* in a linked list.
* @list: the linked list
* Return: 0 if no cycle, 1 if cycle presen
* t
*/
int check_cycle(listint_t *list)
{
listint_t *slw, *fst;

slw = fst = list;
while (slw && fst && fst->next)
{
slow = slw->next;
fast = fst->next->next;
if (slw == fst)
return (1);
}
return (0);
}
