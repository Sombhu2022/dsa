# intupt -> arr= [1,2,3,4,5,6] , n=6

arr = [1,2,3,4,5,6]
n=len(arr)
res =''
for i in range(n):
    if arr[i]%2 == 0:
        res += 'even'
    else:
        res += 'odd'
print(res)
