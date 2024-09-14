def fun(arr , n , ele , diff):
    count = 0
    for i in range(n):
        if arr[i]-ele <= diff:
            count+=1
    return count

n = int(input("enter the length of array"))
list = []
print("enter the array element")
for i in range(n):
    list.append(int(input()))
ele = int(input("enter diff ele"))
diff = int(input("enter diff num"))

res = fun(list , n , ele , diff)
print(res)