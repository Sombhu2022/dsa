# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
arr = [-3,-1,-2,-4]
temp =[]
sum =0
for i in range(len(arr)):
    for j in range(i , len(arr)):
        temp.append(arr[j])
        min_value = min(temp)
        sum += min_value
    temp =[]
print(sum)