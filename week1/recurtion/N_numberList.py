# n =5
# return [1,2,3,4,5]
# using recurtion 

n = int(input('enter range'))
arr=[]

def f(n):
	if n>0:
		arr.append(n)
		f(n-1)

f(n)
r=arr.sort()
print(r)