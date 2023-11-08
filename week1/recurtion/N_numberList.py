# n =5
# return [1,2,3,4,5]
# using recurtion 

n = int(input('enter range'))
arr=[]

def f(n,arr):
    if n>0:
        f(n-1,arr)
        return arr.append(n)
    else:
        return arr

f(n,arr)
print(n,arr)