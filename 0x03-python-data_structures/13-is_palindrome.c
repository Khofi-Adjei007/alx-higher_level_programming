#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return 1;

	/* Find the middle element of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	/* Adjust pointers for odd or even number of nodes */
	if (fast != NULL)
		slow = slow->next;

	/* Compare the first half with the reversed second half */
	while (slow != NULL)
	{
		if (slow->n != prev->n)
		{
			palindrome = 0;
			break;
		}
		slow = slow->next;
		prev = prev->next;
	}

	/* Restore the original structure of the linked list */
	fast = temp;
	while (temp != NULL)
	{
		prev = temp->next;
		temp->next = fast;
		fast = temp;
		temp = prev;
	}

	*head = fast;
	return palindrome;
}
