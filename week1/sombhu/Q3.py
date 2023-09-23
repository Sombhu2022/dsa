
# 3. *Question: List Reversal*
#    - Input: `[1, 2, 3, 4, 5]`
#    - Expected Output: `[5, 4, 3, 2, 1]` (reversed list)

n = int(input('enter the range :'))
arr=[]


print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print('before the array',arr)

#print(arr[::-1])
print('after the array')

for i in range(len(arr)-1 ,-1,-1):
   print(arr[i])


 
