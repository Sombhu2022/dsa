s = "abcde"
g = "cdeab"

s_l = list(s)
g_l = list(g)
size = len(g_l)
print(s_l , g_l)
pop_val =""
for i in range(size):
    pop_val= g_l.pop(0)
    g_l.append(pop_val)
    
    if s_l == g_l : 
        print("true")
        break
if s_l != g_l:
    print("false")