# nums=[1,5,3,2,2,7,6,4,8,9]
# output = [2,10]


nums=[1,5,3,2,2,7,6,4,8,9]

n =len(nums)
total = sum(nums)
actually_total = (n*(n+1))//2

dup = total - sum(set(nums))

f=total-dup   
print(dup , actually_total-f )



