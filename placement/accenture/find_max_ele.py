# find max element with there index 

def fun(arr , n):
    max = arr[0]
    max_index = 0
    for i in range(1 , n):
        if max < arr[i]:
            max = arr[i]
            max_index = i
    return max , max_index

arr = [ 2 , 7 , 5, 9, 45 , 34 ,7 ]
max_val , max_index = fun(arr , len(arr))
print(max_val , max_index)
print(4 == float(4))
        