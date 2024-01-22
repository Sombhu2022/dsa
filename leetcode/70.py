
# 70. Climbing Stairs

a=1 
b=2
sum =0 
count =0
n=3
print(a , b)
for i in range(n+1):
    sum = a+b
    a=b
    b=sum
    count += sum
    print(sum)
    
print("ans:---->",count)