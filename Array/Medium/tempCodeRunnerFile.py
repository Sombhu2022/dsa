for i in range(right , left-1 , -1):
    ans.append([buttom][i])
    buttom-=1
for i in range(buttom , top-1 , -1):
    ans.append([i][left])
    left+=1
print(ans)