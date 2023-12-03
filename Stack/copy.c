#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

// Function to initialize the stack
void initialize(int stack[], int *top) {
    *top = -1;
}

// Function to check if the stack is empty
int isEmpty(int *top) {
    return *top == -1;
}

// Function to check if the stack is full
int isFull(int *top) {
    return *top == MAX_SIZE - 1;
}

// Function to push an element onto the stack
void push(int stack[], int *top, int value) {
    if (isFull(top)) {
        printf("Stack overflow\n");
        return;
    }
    stack[++(*top)] = value;
}

// Function to pop an element from the stack
int pop(int stack[], int *top) {
    if (isEmpty(top)) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return stack[(*top)--];
}

// Function to get the top element of the stack without removing it
int peek(int stack[], int *top) {
    if (isEmpty(top)) {
        printf("Stack is empty\n");
        exit(EXIT_FAILURE);
    }
    return stack[*top];
}

int main() {
    int myStack[MAX_SIZE];
    int top;

    initialize(myStack, &top);

    push(myStack, &top, 10);
    push(myStack, &top, 20);
    push(myStack, &top, 30);

    printf("Top element: %d\n", peek(myStack, &top));

    printf("Popped element: %d\n", pop(myStack, &top));
    printf("Popped element: %d\n", pop(myStack, &top));

    printf("Is the stack empty? %s\n", isEmpty(&top) ? "Yes" : "No");

    return 0;
}
