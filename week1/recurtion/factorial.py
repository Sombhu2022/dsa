n=int(input('enter the number :'))

def f(n,fact)->int:
	if n == 0:
		return fact
	fact *= n 
	f(n-1 , fact)


fact = 1
res=f(n,fact)
print(res)