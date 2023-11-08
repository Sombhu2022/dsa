n = int(input("enter the range of array:"))
arr=[]
# def swap(arr[i],arr[j]):
#     arr[i] , arr[j] = arr[j] , arr[i]
#     return 
def reverse(i,arr , n):
    if i>=n/2: return
    arr[i] , arr[n-i-1] = arr[n-1-i] , arr[i]
    return reverse(i+1, arr , n) 
for i in range(n):
    arr.append(input())

reverse(0,arr,n)
print("array is ")
for i in range(n): print(arr[i])



