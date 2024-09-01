arr = [ 1,5,3,4,7,8,9,1,2]

for i in range(len(arr)):
    if arr[i]%2 == 0:
        for j in range(i+1 , len(arr)):
            if arr[j]%2 != 0:
                arr[i] , arr[j] = arr[j] , arr[i]
                break
print(arr)