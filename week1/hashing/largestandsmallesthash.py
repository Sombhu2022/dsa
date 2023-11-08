#large and small element .
n=int(input("enter the range of array: "))
arr=[]

print("enter array element : ")
for i in range(n):
    arr.append(int(input()))

hash = [0]*1000000 #hashing concept is apply to 10^6

for i in range(n):
    hash[arr[i]] +=1 #pre compute.........hash[10000000] , 50 .. hash[50] +=1 

bigIndex=hash[arr[0]]
smallIndex=None
bigValue=smallValue=arr[0]
for i in range(n):
    if bigIndex<hash[arr[i]]:
        bigIndex=hash[arr[i]]
    if smallIndex is None or smallIndex>hash[arr[i]]:
        smallIndex=hash[arr[i]]
    if bigValue<arr[i]:
        bigValue=arr[i]
    if smallValue > arr[i]:
        smallValue=arr[i]
    
print("largest and smallest index are .",bigIndex,smallIndex)
print('large value and small value are .',bigValue,smallValue)
        
   
