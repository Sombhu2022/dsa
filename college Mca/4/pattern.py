# 55555
# 4444
# 333
# 22
# 1

for i in range(5,0 , -1):
    print(f'{i}'*i )
    




    #      1
    #     2 3
    #    4 5 6
    #   7 8 9 10
num = 1     
for i in range(1,5):
    print(" "*(4-i) , end="")
    for j in range(1,i+1):
        print(num , end=" ")
        num += 1
    print()
 
    
num = int(input("enter number"))
sum =0
num = str(num)
for i in num:
    sum = sum + int(i)
print(sum)





    
#     *
#    * *
#   * * *
#  * * * *


for i in range(1,5):
    print(" "*(4-i) , end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
        


#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *
n =int(input("enter range"))
for i in range(1 , n+1):
    print(" "*(n-i) , end="")
    print("* "*i)
    if i == n :
        for i in range(n-1, 0 , -1):
            print(" "*(n-i) , end="")
            print("* "*i)

# 1
# 2 3
# 4 5 6
# 7 8 9 10
number =1
for i in range(1,5):
    for j in range(i):
        print(number , end=" ")
        number +=1
    print()
        

                
            
            
       