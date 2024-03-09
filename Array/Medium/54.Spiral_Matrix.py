# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

r = len(matrix)
c= len(matrix[0])

top =0 
left =0
right =c-1
buttom = r-1
ans =[]

while(left <= right and top <=buttom):
    for i in range(left , right+1):
        ans.append(matrix[top][i])
    top += 1
    
    for i in range(top , buttom+1):
        ans.append(matrix[i][right])
    right-=1
    
    if( top <= buttom):
        for i in range(right , left-1 , -1):
            ans.append(matrix[buttom][i])
        buttom-=1
    if(left <= right):
        for i in range(buttom , top-1 , -1):
            ans.append(matrix[i][left])
        left+=1

print(ans)
    