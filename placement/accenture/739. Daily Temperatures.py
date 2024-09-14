
def fun(arr , n):
    ans = []
    for i in range(n):
        max_ind = 0
        for j in range(i+1 , n):
            if arr[i] < arr[j]:
                max_ind = j
                break
        if max_ind == 0:
            ans.append(0)
        else:
            ans.append(max_ind - i)
    return ans
                
arr = [71 , 71 , 74 , 69 , 68 , 76 , 78]
res = fun(arr , len(arr))
print(res)