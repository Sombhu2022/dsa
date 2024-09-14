def fun(arr , n):
    res = []
    pos = []
    nag = []
    if n<1:
        return []
    for i in range(n):
        if arr[i] > -1 :
            pos.append(arr[i])
        else:
            nag.append(arr[i])
    i ,j=0,0
    while i< len(pos) or j<len(nag):
        if(i<len(pos)):
            res.append(pos[i])
            i +=1
        if(j<len(nag)):
            res.append(nag[j])
            j +=1
    return res
            

arr = [3, 5, 6 , -3,-9,-1,0,-5]
n= len(arr)

res = fun(arr, n)
print(res)