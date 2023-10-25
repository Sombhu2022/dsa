# input -> n=5 , arr= [1,2,3,4,5] , rotate=3
#output -> arr=[4,5,1,2,3]

n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))
rotate = int(input('input number of how many element are rotate'))

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    temp=[]
    k=0
    for i in range(rotate):
        temp.append(arr[i])
    
    for i in range(rotate,n):
        arr[i-rotate]=arr[i]
    for j in range(rotate , n):
        arr.append(temp[k])
        k+=1
    
    return arr

result = rotateArray(arr , n)
print(result)
