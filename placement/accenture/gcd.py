a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
gcd = 1


if(a==b):
    print(a, "is gcd")

for i in range(1 , min(a,b)+1):
    if a%i == 0 and b%i ==0:
        gcd = i
        print(gcd , a ,b)
   
print(gcd , "is gcd")


print("lcm = " , a*b // gcd)