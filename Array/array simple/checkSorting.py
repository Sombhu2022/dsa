n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))

def isSortedArray(n: int,  a: [int]) -> int:
    # Write your code here.
    
    for i in range(1,n):
        if a[i-1]>a[i]:
            return 0
    return 1
    
res = isSortedArray(n,arr)

if res:
    print('array is sorted')
else :
    print('array is unsorted')


