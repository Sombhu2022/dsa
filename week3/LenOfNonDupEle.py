###################### coding ninja qustion ##################################

n=int(input('enter range'))
arr=[]
for i in range(n):
    arr.append(int(input()))


def removeDuplicates(arr,n):
    # Write your code here.
    ans = []
    for i in range(n):
        if arr[i] not in ans:
            ans.append(arr[i])
    return len(ans)
ans=removeDuplicates(arr,n)
print(f'total ${ans} unique element are present ')