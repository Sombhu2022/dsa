matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]
          ]

r= len(matrix)
c= len(matrix[0])
ans =[[0]*c]*r
print(ans)

for i in range(r):
    for j in range(i):
        matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
for i in range(r):
    matrix[i].reverse()
print(matrix)