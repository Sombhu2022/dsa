# input  s = ABC , in this example A is vowel so , it is fix . and other two charecter are permuting . 
# output is 2 => 2! 

s="ACBehretfj"
n= len(s)
vowel = ['A','E','I','O','U' , 'a','e','i','o','u']
count =0
result = 1
res = 1
for i in range(n):
    if s[i] not in vowel:
        count +=1
        result *=count
        print(s[i], count , result)
    else:
        count =0
        res *= result
        result =1
        print(s[i],count , result , res)
        
    if i == n-1 and s[i] not in vowel:
        res *= result
         
print(res)