n=int(input('enter the number :'))

def f(n)->int:
	if n <=1:
		return 1
	return n*f(n-1)



res=f(n)
print(res)