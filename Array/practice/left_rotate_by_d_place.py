
def arrRotate(arr , d):
    size = len(arr)
    d = d%size
    temp = arr[0:d]
    for i in range(d , size):
        arr[i-d] = arr[i]
    for i in range(size-d , size):
        arr[i] = temp[i-(size-d)]
    return arr

n = int(input('array size'))
arr =[]
for i in range(n):
    arr.append(int(input()))
d = int(input('rotateing position'))
print(arrRotate(arr , d))