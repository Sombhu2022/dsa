# sum of the even position from the reverce array ...

arr = [2,5,3,5,7,9,2]
n=len(arr)
sum_even_pos_value = 0
# first rev the arr 
arr.reverse()
print(arr)
# then find even pos and sum value
for i in range(n):
    if i%2 == 0:
        sum_even_pos_value += arr[i]

print(sum_even_pos_value)