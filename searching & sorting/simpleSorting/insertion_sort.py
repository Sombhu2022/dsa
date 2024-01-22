


arr =[77,33,11,6,22,88,44,8,2,66,-7,-0]
n=10


for i in range(n):
    j=i
    
    print(i , "step :" ,arr)
    while(j>0 and arr[j]>arr[j]):
        arr[j-1] , arr[j] = arr[j] , arr[j-1]
        j=j-1 
    print(arr ,"\n\n")
    
    