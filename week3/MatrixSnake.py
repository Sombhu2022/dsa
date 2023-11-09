matrix = [[1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]
          
          ]
row=len(matrix)
col=len(matrix[0])

def forword(inerarray):
    for i in inerarray:
        print(i,end="  ")
 
def backtrack(inerarray):
    for i in range(col-1,-1,-1):
        print(inerarray[i],end="  ")       
    


print(0%2)
for i in range(row):
    if i%2 == 0:
        forword(matrix[i])
    else :
        backtrack(matrix[i])
    
#in process ....