# 2 SUM 

# ADD 2 ELEMENT in the array .

# input:- [2, 6 , 5, 8 , 7, 9, 4]  , target = 14
# output : 'YES' , [ 1 , 3]

# we use three approch to solve this problem 

# 1. Brute Froce Method :-
        
        
# 2. Hashing 
# 3. Two Pointer 


# using Hashing , use extra space for hash table
arr = [-4, 2, 6 , 4 , 7 , -6 , 9 ,5]
target = 10
hash = { }
count = 0 

for i in range(len(arr)):
    a = arr[i]
    sec = target-a
    
    if sec in hash:
        print("indexs are ", hash.get(sec) ,i  )
        count = 1
        break
    hash[a] = i
if count == 0 : print("no")



# using two pointer

print("**  using two pointer   **")
copy=arr.sort()   #[2, 4 , 5 , 6  , 7 , 9 ]  #O(n)
size = len(arr)
i = 0
j=size-1

while(i < j): #O(n)
    sec = target - copy[i]
    if sec == copy[j]:
        print("index are ", i ,j)
        break
    elif sec < copy[j] :
        j -=1
        # print("j-" , j)
    else:
        i += 1
        
    
# total time complexcity O(2n) , space O(1)
    

        
   

