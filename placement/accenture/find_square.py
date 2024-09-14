import math
def fun(arr , n):
    count = 0
    
    for i in range(n):
     
        square = math.sqrt(arr[i])
        if square == int(square):
            count +=1
    return count
            

n = 6 
arr = [64 , 19 , 16 , 81 , 100 , 20]
res = fun(arr , n)
print(res)