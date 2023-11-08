n= int(input("enter the range of fibonacci number : "))

def fib(n):
    if n <=1: return n
    return fib(n-1)+fib(n-2)

print("fibonacci numbers are:")
for i in range(n):
    result = fib(i)
    print(result)

    