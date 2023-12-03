#include<stdio.h>

#define max_size 10


int stack[max_size];
int top =-1;
int empty(){
    return top<0;

}

int stackfull(){
    return  top == max_size-1 ;
}

void push(){
    int element;
     printf("\npush func");
   if (stackfull()){
       printf("Stack is overfllow");
       
   } else{
        printf("enter the element");
        scanf("%d",&element);
        top++;
        stack[top]= element;
        
             
   }


}

void show(){
    int i;
     if(empty()){
        printf("\nstack is underfllow");
    }
   printf("\nshow function");
   for(i=top; i>-1;i--){
        printf(" <- %d ", stack[i]);

   }
    // while(! empty()){
    //     printf(" <- %d ", stack[top]);
    //     top--;
    // }

}

void pop(){
    if(empty()){
        printf("\nstack is underfllow");
    }
    else{
        top--;
    }
}

int main(){
    
    printf("enter the range of the stack");
    // scanf("%d",&n);
    push();
    push();
    show();
    pop();
    show();
    pop();
    show();
    pop();
 return 1;
    
}