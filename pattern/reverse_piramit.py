n=5
print(n)
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    print('* '*i)
    
n=5
for i in range(n,0,-1):
    print(f'{i}'*i)
    
r=[9,4,3,5,2,67,9]

l = [ 0 ] * max(r)
print(l)

my_dict = {key: 0 for key in range(10)}
print(my_dict)

