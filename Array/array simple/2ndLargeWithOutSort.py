
arr = [12 , 12]

large = float('-inf')
second_large = float('-inf')

for i in range(len(arr)):
    if arr[i] > large:
        second_large = large
        large = arr[i]
    elif arr[i] > second_large and arr[i] != large:
        second_large = arr[i]
        
if( second_large == float('-inf')):
    print(-1)
else :
    print(second_large)