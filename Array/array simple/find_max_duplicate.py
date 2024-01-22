print("find max duplicate in an array")

arr = [1,1,1,4,4,4,4,2,2,2,3,3,3, 3,4,8,2]

#  hashing approch
maxv = max(arr)
hasht = [0]*(maxv+1)

for i in range(len(arr)):
    hasht[arr[i]] += 1
ans = max(hasht)
print(hasht.index(ans))

arr.sort() #[1,1,1,3,3,3,3,4,4,5,5,5,5,5]
j=0
size=len(arr)
count = 0
max = 0
for i in range(size):
    if arr[i] != j:
        j = arr[i]
        count +=1
        if max < count:
            max = count
            count =0
    elif arr[i] == j:
        count +=1
print(max)
        
        

