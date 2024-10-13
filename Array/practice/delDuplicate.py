# delete duplicate value from the sorted array 


# approch 1 : ---> create a ans array then find unique element and store this element in ans array 

arr = [ 2,2 , 3 ,4 , 5,5 , 5 ,5 , 6,7 ,8 ,9,9]
ans = []

for i in range( len(arr)):
    if arr[i] not in ans:
        ans.append(arr[i])

print(ans)
        

# approch 2 : ---> convert array to set ..

print(list(set(arr)))