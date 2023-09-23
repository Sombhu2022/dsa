# 6. *Question: Palindrome Check*
#    - Input: `"racecar"`
#    - Expected Output: `True` (the word is a palindrome)

string = str(input('enter the range :'))

string = string.strip()

reverse= string[::-1]

if string:

   if string == reverse :
      print(f'{string } :-- is a armstrong ')
   else :
      print(f'{string}  :-- is not armstrong')

else :
      print(f' string :-- is empty ...⚠️ input valid words')


   