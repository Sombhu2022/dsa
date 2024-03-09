# 128. Longest Consecutive Sequence

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

nums = [9,1,4,7,3,-1,0,5,8,-1,6,7,7,7,7]
set = set(nums)
new_set = sorted(set)
print(new_set)
cnt=nums[0]
count = 1
inc=1

for i in range(1,len(new_set)):
    if cnt + inc == new_set[i]:
        inc +=1
        count+=1
    else:
        cnt = new_set[i]
        inc =1
    count = max(count , inc)
print(count)