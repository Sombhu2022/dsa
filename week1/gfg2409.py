n = int(input('enter the range :'))
arr=[]
duplicate =[]
print('enter the arr element')
for i in range(n):
   arr.append(int(input()))

print(arr)


	arr=arr.sort()
    	duplicate=[]

    	for i in range(n-1):
    	    if arr[i] == arr[i+1]:
    	        if arr[i] not in duplicate:
    	            duplicate.append(arr[i])
    	        
    	 
    	
    	if duplicate :
    	    return duplicate
    	else :
    	    return [-1]
    	        