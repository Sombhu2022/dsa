#input 132456
#output 12 9 .... 2+4+6=12 , 3+5+1=9

n = int(input('enter the number :'))

sumEven=0
sumOdd=0

if n:
	while n > 0:
		digit= n%10

		if digit%2==0:
			sumEven += digit
		else:
			sumOdd += digit

		n=int(n/10)

	print('Sum of Even digit',sumEven ,'  Sum of odd digit' , sumOdd)

else:
	print('Sum of Even digit',0 , '  Sum of odd digit' , 0)



			

