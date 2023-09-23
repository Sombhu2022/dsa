# 2. *Question: Factorial Calculation*
#    - Input: `5`
#    - Expected Output: `120` (5 factorial)

num = int(input('enter the number :'))

def factorial(num):
   f=1
   for i in range(1,num+1):
      f*=i
   return f

result=factorial(num)
print('factorial is : ',result)




