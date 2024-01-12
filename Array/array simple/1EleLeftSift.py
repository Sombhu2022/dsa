# input -> n=5 , arr= [1,2,3,4,5]
#output -> arr=[2,3,4,5,1]

n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

result = rotateArray(arr , n)
print(result)
