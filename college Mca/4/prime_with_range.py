n = int(input("enter the range "))

print("prime serise is")
for i in range(2,n+1):
    count = 0
    for j in range(2, i//2+1 , 1):
        if i%j == 0:
            count +=1
    if count == 0:
        print(i)
        