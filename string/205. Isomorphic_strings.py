s1 = "add"
s2 = "ego"

if len(s1) != len(s2): print("false")
else:
    c1 , c2 = "" , ""
    hash_map_s1 = {}
    hash_map_s2 = {}
    
for i in range(1,len(s1)):
    c1 , c2 = s1[i] , s2[i]
    if ((c1 in hash_map_s1 and hash_map_s1[c1] != c2) or (c2 in hash_map_s2 and hash_map_s2[c2] != c1)):
        print("false")
        break
    hash_map_s1[c1] = c2
    hash_map_s2[c2] = c1

print("true")