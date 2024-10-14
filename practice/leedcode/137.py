# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.

nums = [0,1,0,1,0,1,99]
once = None
nums.sort()
size = len(nums)
if size == 1:
    once = nums[0]
for i in range(0,len(nums)-1):
    if nums[i] != nums[i+1]:
        if i ==0:
            once = nums[i]
        elif i+1 == size-1:
            once = nums[i+1]
        elif nums[i+1] != nums[i+2]:
            once = nums[i+1]
print(once)
    
         