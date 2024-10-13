#  All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

arr = [1,4,0,3,0,0,0,0,0,5,0,2,0,0,5,6,7]
size = len(arr)

# approch 1 

for i in range(size):
    if arr[i] == 0:
        for j in range(i+1 , size):
            if arr[j] != 0:
                arr[i] , arr[j] = arr[j] , arr[i]
                break

print(arr)

# approch 2

arr2 = [1,4,0,3,0,0,0,0,0,5,0,2,0,0,5,6,7]
size2 = len(arr2)
j =0

for i in range(size2):
    if arr2[i] != 0 and arr2[j] == 0:
        arr2[i] , arr2[j] = arr2[j] , arr2[i]
    if arr2[j] != 0:
        j +=1
print(arr2)