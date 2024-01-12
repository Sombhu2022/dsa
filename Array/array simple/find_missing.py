l= [-1 , -3 , 4 , 4 , 4 , 3  , 3, 9 , 9 , 9, 7, 7 ,-3]
hash = {
    
}

for i in range(len(l)):
    hash[l[i]]= 0
    
for i in range(len(l)):
    hash[l[i]] += 1
    
for key, value in hash.items():
    if value == 1:
        keys_with_value_1 = key

print("Keys with value 1:",keys_with_value_1 )
print(hash)

