#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the initial linked list pointer
 * @number: number to insert
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;
	int i, j;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number, temp = *head;
	if (!(*head))
		return (*head = new, new->next = NULL, new);
	for (i = 0; temp; i++)
	{
		if (number > temp->n)
		{
			if (!temp->next)
				return (temp->next = new, new->next = NULL, new);
			temp = temp->next;
			continue;
		}
		else
		{
			new->next = temp;
			if (temp == *head)
			{
				*head = new;
				break;
			}
			temp = *head;
			for (j = 0; j < i; j++)
			{
				if (j == (i - 1))
				{
					temp->next = new;
					break;
				}
				temp = temp->next;
			}
			break;
		}
	}
	return (new);
}
