n = int(input('enter range'))

def f(n):
	if n>0:
		f(n-1)
		print(n)

f(n)