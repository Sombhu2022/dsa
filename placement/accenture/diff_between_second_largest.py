# def LargeSmallSum(arr)

# The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

# Assumption:

# All array elements are unique
# Treat the 0th position as even
# NOTE

# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3
# Example

# Input

# arr:3 2 1 7 5 4

# Output

# 7

# Explanation

# Second largest among even position elements(1 3 5) is 3
# Second smallest among odd position element is 4
# Thus output is 3+4 = 7
# Sample Input

# arr:1 8 0 2 3 5 6

# Sample Output

# 8

def diff_arr_ele(arr):
    if  len(arr) <= 3: return 0
    even_arr = arr[::2]
    odd_arr = arr[1::2]
    even_arr.sort()
    odd_arr.sort()
    return even_arr[len(even_arr)-2] + odd_arr[1]

arr = [1 ,8 ,0 ,2 ,3 ,5 ,6]
arr2 =[6 , 8 ,9 , 8]
res = diff_arr_ele(arr2)
print(res)
    