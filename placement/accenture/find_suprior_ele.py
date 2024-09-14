# find total number of suprior element in an element , 

# note - rightmost element alrady a suprior element

def fun(arr , n):
    count = 1
    max = arr[0] 
    for i in range(1 ,n):
        if max < arr[i]:
            print(arr[i])
            count +=1
            max = arr[i+1]
    return count

n = 6 
arr = [8 , 10 , 6 , 2 , 9 ,7]
res = fun(arr , n)
print(res)