
# 5. *Question: Find Maximum Value*
#    - Input: `[10, 3, 15, 7, 2]`
#    - Expected Output: `15` (maximum value in the list)

n = int(input('enter the range :'))
arr=[]

print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print(arr)

#print('max value in the list  is ' ,max(arr))

maxValue=arr[0]
for i in arr:
   if maxValue <i:
      maxValue = i

print('max value in the list  is ' ,maxValue)
