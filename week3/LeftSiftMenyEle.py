# input -> n=5 , arr= [1,2,3,4,5] , rotate=3
#output -> arr=[4,5,1,2,3]
#leedcode problem

n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))
r = int(input('input number of how many element are rotate'))


def rotateArray(arr: [], n: int , r:int) -> []:
    # Write your code from here.
    r = r%n
    temp=[]
   
    for i in range(r):
        temp.append(arr[i])
    
    for i in range(r, n):
        arr[i-r] = arr[i]
        
    for i in range( n-r, n):
        arr[i]=temp[i-(n-r)]
       
    
    return arr


result = rotateArray(arr , n ,r)
print(result)
