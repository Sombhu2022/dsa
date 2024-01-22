# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

copy = []
lis = [1, 1]


n=0
ans= [[0 for j in range(i+1)] for i in range(n)]

# def fun(n):
#     if n == 1:
#         return [[1]]
#     return fun(n-1 , )
    

for i in range(n):
    for j in range(i+1):
        if j == 0 or j ==i:
            ans[i][j] = 1
        else:
            ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
print(ans)
            
    
    