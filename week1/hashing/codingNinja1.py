n=int(input("enter the range of array: "))
arr=[]
ans=[]
x=int(input("enter the range of element"))
print("enter array element : ")
for i in range(1,n+1):
    val=int(input())
    if val<1 or val>x:
        print("value range 1 to ",x)
        i-=1
    else:
        arr.append(val)

hash = [0]*(x+1) #hashing concept is apply to 

for i in arr:
    hash[i] +=1 #pre compute.........

for i in arr:
    ans.append(hash[i])
        
