def fun(n):
    b = n *2 
    for i in range(n-1 , 0 , -1):
        b += i*3
    return b
            
n = 3
res = fun(n)
print(res)