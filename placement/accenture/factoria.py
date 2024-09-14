
p = 1
for i in range(1 , 11):
    p =1
    for j in range(i , 0 , -1):
        p  *=  j 
        
    print( i , "! = " , p , 2 ** i)
    