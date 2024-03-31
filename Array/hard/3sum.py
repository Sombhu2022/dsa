# this is three sum problem 

arr=[-1 , 0 , 1,2,-1,-4]
arr.sort()
print(arr)
n = len(arr)
ans =[]
print(ans)
for i in range(n):
    if i !=0 and arr[i] == arr[i-1]:
        continue
    j=i+1 
    k = n-1
    while j < k :
        print(i ,j ,k)
        total_sum = arr[i]+arr[j]+arr[k]
        if total_sum > 0:
            k = k-1
        elif total_sum <0:
            j = j+1
        else :
            temp = [arr[i], arr[j], arr[k]]
            ans.append(temp)
            j += 1
            k -= 1
            # skip the duplicates:
            while j < k and arr[j] == arr[j - 1]:
                j += 1
            while j < k and arr[k] == arr[k + 1]:
                k -= 1

print(ans)