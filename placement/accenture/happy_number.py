# find happy number ..
# ex:-
# n = 19 
#  1^2 + 9^2 = 82  ->  8^2 + 2^2 = 68  -> 6^2 + 8^2 = 100  -> 1^2 + 0^2 + 0^2 = 1 -> "1" so 19  is happy number

def fun(n):
    list = set()
    while n!= 1 and n not in list:
        sum = 0 
        list.add(n)
        for i in str(n):
            sum += int(i)**2
            n = sum
    
    return n == 1        
            
        

n = 1340 
res = fun(n)
print(res)