# 9. *Question: Count Occurrences*
#    - Input: `[1, 2, 2, 3, 4, 2, 5]`
#    - Expected Output: `3` (number of times '2' appears in the list)


n = int(input('enter the range :'))
arr=[]

print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print(arr)

value =int(input('entr the finding value :'))

count=0

for i in arr:
   if i == value:
      count += 1

print(f'{count}  number of times  {n} appears in the list')
