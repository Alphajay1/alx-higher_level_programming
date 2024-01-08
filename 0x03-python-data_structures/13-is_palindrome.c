#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: The head of the singly linked list
 *
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int idx = 0, len = 0, len_cycle = 0, list_len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	start = *head;
	len = listint_length(start);
	len_cycle = len * 2;
	list_len = len_cycle - 2;
	end = *head;

	for (; idx < len_cycle; idx = idx + 2)
	{
		if (start[idx].n != end[list_len].n)
			return (0);

		list_len = list_len - 2;
	}
	return (1);
}

/**
 * nodeint_at_index - get the node from a linked list
 * @head: head of the linked list
 * @index: index to find in linked list
 *
 * Return: node of the linked list
 */
listint_t *nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int i = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (i == index)
				return (current);

			current = current->next;
			i++;
		}
	}
	return (NULL);
}

/**
 * listint_length - gives elements in a linked list
 * @a: the linked list to count
 *
 * Return: number of elements in the linked list
 */
size_t listint_length(const listint_t *a)
{
	int len = 0;

	while (a != NULL)
	{
		++len;
		a = a->next;
	}
	return (len);
}
