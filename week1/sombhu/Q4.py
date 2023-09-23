# 4. *Question: Check Prime Number*
#    - Input: `7`
#    - Expected Output: `True` (7 is a prime number)

n=int(input('enter the number: '))
count =0

for i in range(1,int(n/2)+1,1):
   if n%i ==0:
      count +=1

if count == 1 :
   print(f'{n} is prime .... ')

else :
   print(f'{n} is not prime .... ')
