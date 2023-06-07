#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list is cyclical
 * @list: pointer to the head of the linked list
 * Return: 1 if the list is cyclical, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list; /* Pointer moving one node at a time */
	listint_t *fast = list; /* Pointer moving two nodes at a time */

	while (fast && fast->next)
	{
		slow = slow->next; /* Move slow pointer by one node */
		fast = fast->next->next; /* Move fast pointer by two nodes */

		/* If the slow and fast pointers meet, the list is cyclical */
		if (slow == fast)
			return (1);
	}

	/* If the fast pointer reaches the end of the list, it is not cyclical */
	return (0);
}
