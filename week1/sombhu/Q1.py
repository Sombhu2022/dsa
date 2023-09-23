# 1. *Question: Sum of Even Numbers*
#    - Input: `[1, 2, 3, 4, 5, 6]`
#    - Expected Output: `12` (sum of even numbers)

n = int(input('enter the range :'))
arr=[]

print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print(arr)

sumEven=0

print('output......')
if arr:
   for i in arr:
      if i % 2 ==0:
         sumEven += i
   print( sumEven )
else :
   print(sumEven)



