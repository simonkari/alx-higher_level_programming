#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - function to see if list is palindrome
 * @head: ptr at the beginning
 * Return: 0 not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);
return (check_pal(head, *head));
}

/**
 * check_pal - function to see if the list is palindrome
 * @head: ptr at the beginning
 * @last: ptr at the end
 * Return: 0 not palindrom else 1
 */
int check_pal(listint_t **head, listint_t *last)
{
if (last == NULL)
return (1);
if (check_pal(head, last->next) && (*head)->n == last->n)
{
*head = (*head)->next;
return (1);
}
return (0);
}