#include<stdio.h>
#define MAX_SIZE 10
int Queue[10],front=-1,rear=-1;

int empty(){
    if (front == -1 && rear == -1)
    {
        return 1;
    }
    return 0;
    
}

void printQueue(){
    int i=0;
    if(empty()){
        printf("Queue is empty");
    }
    else{

    for ( i = front ; i <= rear; i++)
    {
       printf(" %d->%d  | ", i, Queue[i]);
    }
    printf("\n\n");
    }
    
}

// time complexcity of enqueue in linear queue O(1)
void enqueue(int element){
    if(rear+1 == MAX_SIZE){
        printf("Queue is alrady full");
    }
    else{
       if (front == -1) front = front+1;
    rear=rear+1;
    Queue[rear] = element ;
    printQueue();
   }
}

// time complexcity of dequeue in linear queue O(1)

void dequeue(){
    
    if(empty()) 
    {

    printf("Queue is alrady empty");
    }
    else{
        if( front == rear) 
        {front = rear=-1;}
       else{ front = front+1;
       printQueue();
       }
    }
}


int main(){
    printQueue();
    enqueue(9);
    enqueue(8);
    dequeue(); // delete 9
    enqueue(0);
    enqueue(5);
    enqueue(3);
    enqueue(2);
    enqueue(7); 
    dequeue(); // delete 8
    enqueue(0);
    enqueue(8);
    enqueue(6);
    enqueue(8);
    enqueue(4);
    enqueue(1);
}