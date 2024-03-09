matrix=[
    [1,2,1,0],
    [3,4,6,7],
    [0,9,5,4],
    [0,5,6,0]
]

r=len(matrix)
c=len(matrix[0])

row =[0]*r
col = [0]*c

print(r ,c , row , col)

for i in range(r):
    for j in range(c):
        if  matrix[i][j] == 0:
            row[i]=1
            col[j]=1

print(row , col)
print()

for i in range(r):
    for j in range(c):
        if row[i] == 1 or col[j] == 1:
            matrix[i][j] = 0
            
print(matrix)
            