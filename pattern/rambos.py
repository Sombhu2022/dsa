n=5
print(n)
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    print('* '*i)
    
    if i==n-1:
        for i in range(n,0,-1):
            for j in range(n-i):
                print(end=" ")
            print('* '*i)