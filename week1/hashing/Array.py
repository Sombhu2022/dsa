#hashing 
n=int(input("enter the range of array: "))
arr=[]

print("enter array element : ")
for i in range(n):
    arr.append(int(input()))
    

hash = [0]*1000000 #hashing concept is apply to 

for i in range(n):
    hash[arr[i]] +=1 #pre compute.........

out=int(input("enter total output : "))

for i in range(out):
    number=int(input())
    if hash[number]:#fetch.........
        print("number of ",number ,"is : " ,hash[number])
    else:
        print(number,"is not exist....")
