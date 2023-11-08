# approch ->  m a d a m --- avery word must be similer to another direction word 

#  0=-1 , 1=-2 , 2=-3  


s = input("enter the string : ")
s=s.lower()
def palindrom(i,s):
    if i>=len(s)/2: return True
    if s[i] != s[len(s)-i-1] :
        return False
    return palindrom(i+1, s) 

result=palindrom(0,s)


if result == True:
    print("this is palindrom")
else:
    print("this is not palindrom")
