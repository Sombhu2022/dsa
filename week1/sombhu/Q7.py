
# 7. *Question: Fibonacci Sequence*
#    - Input: `8`
#    - Expected Output: `[0, 1, 1, 2, 3, 5, 8, 13]` (first 8 numbers in the Fibonacci sequence)

n = int(input('enter the range :'))
fibonacci=[]
total=0
n1=0
n2=1

for i in range(1 , n+1):
   fibonacci.append(total)
   n1 , n2 = n2 , total
   total = n1 +n2 

print(fibonacci)
   
