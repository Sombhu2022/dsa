arr =[1,1,0,1,1,1,0,0,1,1,1,1,1]
count =0
max_val = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
    elif arr[i] == 0:
        max_val = max(max_val , count)
        count = 0

if count != 0:
    max_val = max(max_val , count)

print(max_val)