n = int(input("enter the range:"))

def fun(n):
    if n>0:
        return n+fun(n-1)
    return n 

print(fun(n))