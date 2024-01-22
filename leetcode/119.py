# Input: numRows = 5
# Output: [1,4,6,4,1]

copy = []
lis = [1, 1]


n=5
ans= [[0 for j in range(i+1)] for i in range(n+1)]

# def fun(n):
#     if n == 1:
#         return [[1]]
#     return fun(n-1 , )
    

for i in range(n+1):
    for j in range(i+1):
        if j == 0 or j == i:
            ans[i][j] = 1
        else:
            ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
print(ans[n-1])
            
    
    