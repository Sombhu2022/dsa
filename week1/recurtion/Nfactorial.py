#Factorial Numbers Not Greater Than N

n=int(input("enter the number :"))
ans=[]
val=n
fac=1
def f(n,ans,val,fac):
	if n >0:
		fac =fac* f(n-1,ans,val,fac)
	if val > fac:
		ans.append(fac)
	if val <fac:
		return ans



for i in range(1,n+1):
	f(i,ans,val,fac)