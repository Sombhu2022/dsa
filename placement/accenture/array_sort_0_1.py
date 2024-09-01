arr = [0,0,1,0,1,0,1,0,1]

arr1 = []
arr2 = []

for i in range(len(arr)):
    if arr[i] == 1:
        for j in range(i+1 , len(arr)):
            if arr[j] == 0:
                arr[i] , arr[j] = arr[j] , arr[i]
                break

print(arr)
                
        
        