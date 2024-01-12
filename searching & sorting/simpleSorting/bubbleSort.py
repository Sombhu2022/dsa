

def selectionSort(arr):
    # Write your code here
    pass
    for i in range(len(arr)-1):
    
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j+1] , arr[j] = arr[j],arr[j+1]
    return arr

arr=[5,3,-9,1,2,0]
print(arr)
selectionSort(arr)
print("********after sorting**********")
print(arr)

