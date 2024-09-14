
def fun(arr , n):
    arr.sort()
    count = 0
    for i in range(1,n):
        count += abs(arr[i-1] - arr[i])
    return count
    

n = 3 
arr = [ 1, 3 ,2]
res = fun(arr , n)
print(res)
