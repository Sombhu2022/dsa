

def selectionSort(arr):
    # Write your code here
    pass
    for i in range(len(arr)-1):
        mini=i
        for j in range(i+1 , len(arr)):
            if arr[mini]>arr[j]:
                mini = j
        arr[mini] , arr[i] = arr[i],arr[mini]
    return arr

arr=[5,3,9,1,2,0]
print(arr)
selectionSort(arr)
print("********after sorting**********")
print(arr)