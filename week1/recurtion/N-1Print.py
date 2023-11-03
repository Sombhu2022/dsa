#print N to 1 using recurtion 
n = int(input("enter the range:"))
arr=[]

def f(n,arr):
    if n>0:
        arr.append(n)
        return f(n-1,arr)
    return arr 
f(n,arr)
print(arr)