#include <stdio.h>
#define MAX_SIZE 4
int Queue[10], front = -1, rear = -1;

int empty()
{
    if (front == -1 && rear == -1)
    {
        return 1;
    }
    return 0;
}

int isFull()
{
    return (rear + 1) % MAX_SIZE == front; // whenw
}

void printQueue()
{
    int i;
    if (empty())
    {
        printf("Queue is empty");
    }
    else if (rear >= front)
    {
        for (i = front; i <=  rear ; i++)
        {
            printf("%d , %d |", i, Queue[i]);
        }
    }
    else
    {
        i = front;
        for (i = front; i < MAX_SIZE; i++)
        {
            printf("%d , %d |", i, Queue[i]);
        }

        for (i = 0; i <= rear ; i++)
        {
            printf("%d , %d |", i, Queue[i]);
        }
    }
    printf("\n");
}

// time complexcity of enqueue in linear queue O(1)
void enqueue(int element)
{
    if (isFull())
    {
        printf("Queue is alrady full");
    }
    else
    {
        if (front == -1)
            front = (front + 1) % MAX_SIZE;
        rear = (rear + 1) % MAX_SIZE;
        Queue[rear] = element;
    }
}

// time complexcity of dequeue in linear queue O(1)

int dequeue()
{
    int result;
    if (empty())
    {
        printf("Queue is alrady empty");
    }
    else
    {
        result = Queue[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front = (front + 1) % MAX_SIZE; 

            return result;
        }
    }
}

int main()
{
    // printQueue();
    int choice, result , n;
    while (1)
    {
        printf("enter your choice : \n 1. insert \n 2.delete \n 3.display \n 4.exit\n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("enter the element : ");
            scanf("%d", &n);
            enqueue(n);
            break;
        case 2:
           result = dequeue();
           printf(" delete %d \n" , result);
            break;
        case 3:
            printQueue();
            break;
        case 4:
            printf("exit");
            return 1;

        default:
            printf("choice valid option");
            return 1;
        }
   
    }
}