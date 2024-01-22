# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

n= int(input("enter the range"))
arr=[]
# arr=[1,2,3,4,5,6,7]
for i in range(1,n+1):
    arr.insert(i , int(input()))
r=int(input("how meny value rotet "))

temp =[]
temp = arr[n-r:n+1]
temp2 = arr[1:]
