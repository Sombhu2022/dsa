#input : [1, 4 , 7, 5 ,5 , 5,5 ,7 ,4 ,0]
#output : 3  6 

n = int(input('enter the range :'))
arr=[]

print('enter the arr element')
for i in range(n):
	arr.append(int(input()))

print(arr)
value=int(input('enter the value :'))

firstPos = None
lastPos=None

if n>0:
	for i in range(n):
		if arr[i] == value and firstPos == None:
			firstPos = i
			lastPos = i
		elif arr[i] == value and arr[i-1]== value:
			lastPos = i

	if 	firstPos == None and lastPos==None:
		print(-1 , -1)
	else:
		print( firstPos , lastPos)

else:
	print('plesce input the range more then 0')

	






