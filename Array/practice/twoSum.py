# # two sum problem 

# Example 1:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Result: YES (for 1st variant)
#        [1, 3] (for 2nd variant)
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

# Example 2:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
# Result: NO (for 1st variant)
# 	[-1, -1] (for 2nd variant)
# Explanation: There exist no such two numbers whose sum is equal to the target.




# approch use two pointer 

arr = [2,6,5,8,11]
target = 14
n = len(arr)

# sort the array
arr.sort()

def twoSum(arr , n , target):
    left , right = 0 , n-1
    summ =0
    while left < right:
        summ =  arr[left]+arr[right]
        if target == summ:
           return [left , right ]
        elif target < summ:
            right -=1 
        else:
            left += 1
    return [-1 , -1]

print(twoSum(arr , n , target))