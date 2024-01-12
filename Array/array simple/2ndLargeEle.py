#find second large element an array
n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))

def secondLargeEle(arr: [] , n: int)->int:
    if n >1:
        arr.sort()
        return arr[n-2]
    else :
        return  1
    
ans = secondLargeEle(arr , n)
if ans >1:
    print('second large number an array is ', ans)
else :
    print('second large element are not exist in array')
    