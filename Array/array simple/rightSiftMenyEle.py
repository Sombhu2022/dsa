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

for i in range(n):
    arr.append(int(input()))
r=int(input("how meny value rotet "))
r=r%n
temp =[]
temp[:] = arr[n-r:n] 

for i in range(n-r-1, -1, -1):
    arr[i+r]=arr[i]
for i in range(r):
    arr[i] = temp[i]
print(arr)

        