arr = [1 , 2, 3, 4, 5 ,6]
N = 7

# approch 1 --> best sol

size = len(arr)
arr.sort()
for i in range(1 , N+1):
    if size < i:
        print('missing number is',i)
        break
    elif arr[i-1] != i:
        print('missing number is',i)
        break
    

# approch 2 : --> optimal solution 

total = (N*(N+1))//2
total_of_arr_ele = 0

for i in arr:
    total_of_arr_ele += i

print('missing number is ' , total - total_of_arr_ele)