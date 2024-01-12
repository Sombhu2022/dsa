# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 4, 6]
# ‘b’ = [2, 3, 5]

# Output: [1, 2, 3, 4, 5, 6]

m= 5 
n = 3
a = [1, 2, 3, 4, 6]
b = [2, 3, 5]

a.sort()
b.sort()

set1 = set(a)
set2=set(b)
#union two set .
ans= set1.union(set2)
print(ans)