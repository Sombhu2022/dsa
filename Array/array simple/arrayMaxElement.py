n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    if n:
        arr.sort()
        return arr[n-1]
    else:
        return 0 

ans = largestElement(arr , n)

if ans :
    print('max length is',ans)
else :
    print('array is empty')