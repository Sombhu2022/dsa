# find the union two array
# result will be sorted 
arr1 = [1,3,4,6,3,5,6]
arr2 = [3,5,6,7,8,9,0]
res = []

for i in arr1+arr2:
    if i not in res:
        res.append(i)
res.sort()
print(res)
    