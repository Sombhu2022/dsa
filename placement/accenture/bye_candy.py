# problem statment ->  given a price of candy arr , and a ammount  if array value is divisible by 5 then we not spend money 
#         for candy , otherwise pay a[i] value . bye the maximum number of candy.

arr = [ 2 ,5 , 7, 3, 15 , 20  , 4,6]
m = 10
n = len(arr)
count = 0

arr.sort()
print(arr)

for i in range(n):
    if arr[i]%5 == 0:
        count += 1
    else:
        if m-arr[i] >= 0:
            m = m-arr[i]
            count +=1
        
print(count)