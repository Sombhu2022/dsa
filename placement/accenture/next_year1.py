n = 13 
seq = []
sum =0
for i in range(n/2):
    if i**2 <= n:
        seq.append(i**2)
    else:
        break
seq.sort()
for i in seq:
    sum +=seq[i]
    if sum == n:
        print("step",i)
    elif sum >n:
        print()
        
        
print("un solveed")