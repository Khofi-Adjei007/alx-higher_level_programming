#!/usr/bin/python3
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted list
 * @head: address of the head pointer
 * @number: number to insert
 * Return: pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head; /* Initialize a pointer to the head of the list */
    listint_t *new = malloc(sizeof(listint_t)); /* Allocate memory for the new node */

    if (!new) /* Check if memory allocation was successful */
        return (NULL);

    new->n = number; /* Set the value of the new node to the specified number */
    new->next = NULL; /* Set the next pointer of the new node to NULL */

    /* If the list is empty or the new node has the smallest value,
     * insert the new node at the beginning of the list and update the head pointer */
    if (!node || new->n < node->n)
    {
        new->next = node;
        return (*head = new);
    }

    /* Traverse the list to find the appropriate position to insert the new node */
    while (node)
    {
        /* If the current node is the last node or the value of the new node
         * is less than the value of the next node, insert the new node here */
        if (!node->next || new->n < node->next->n)
        {
            new->next = node->next;
            node->next = new;
            return (node);
        }
        node = node->next; /* Move to the next node */
    }

    return (NULL); /* Return NULL if the node couldn't be inserted */
}
