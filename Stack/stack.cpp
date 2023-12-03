#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    // if(! stack.empty()){
    //     cout<<" stack is empty";
    // }
    while (!stack.empty())
    {
        cout << " <-" << stack.top();
        stack.pop();
    }

    return 1;
}
