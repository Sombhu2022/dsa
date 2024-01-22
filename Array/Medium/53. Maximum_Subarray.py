# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:



nums = [-2,-9,-4,-1]
sum =0
max_sum=float('-inf')

#breute fource method 
for i in range(len(nums)):
    for j in range(i , len(nums)):
        sum += nums[j]
        max_sum = max(sum , max_sum) 
    sum =0
    
print(max_sum)    
    
# time complexcity --> O(n^2)
# space complexcity --> O(1) 


#optimal solution using (kadane's algoritham)
for i in nums: #get all array element ..
    sum +=i #sum array elements one by one ..
    max_sum = max(max_sum , sum) #if sum grater then max_sum then set value of sum into max_sum
    if sum < 0: # if sum smaller then 0 then 0 is set in sum ..
        sum = 0
print(max_sum)
 
# time complexcity --> O(n)
# space complexcity --> O(1) 
 
 