#include "lists.h"

/**
 * print_dlistint - Prints elements of a dlistint_t list.
 * @h: Head of the dlistint_t list.
 * Return: Number of nodes in the list.
 */

size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *current = h;
size_t nodes = 0;

while (h)
{
nodes++;
printf("%d\n", current->n);
current = current->next;
}

return (nodes);
}
