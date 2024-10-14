nums = [100000, 3, 4000, 2, 15, 1, 99999]
j =0
missing = 0
nums=list(set(nums))
nums.sort()
print(nums)
for i in range(len(nums)):
    if nums[i]> 0:
        j+=1
        if nums[i] != j:
            missing = j
            break
print(missing)