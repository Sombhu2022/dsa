list = ['a' , 'a' ,"b" , "c","b"]

fec=dict()

for i in list:
    fecuancy = list.count(i)
    fec[i]=fecuancy
print(fec)

num = int(input("enter num : "))
n= str(num)
rev = n[::-1]
if n == rev:
    print("palindrom")
else:
    print("not")
    