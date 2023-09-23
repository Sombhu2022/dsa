
# 8. *Question: Calculate Average*
#    - Input: `[12, 15, 20, 10, 8]`
#    - Expected Output: `13` (average of the numbers)


n = int(input('enter the range :'))
arr=[]

print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print(arr)
total=0

for i in arr:
   total += i 

print(f'avarage of the numbers are {total/len(arr)}')
