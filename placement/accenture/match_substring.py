s1 = "adventure"
s2 = "future"
sub = ''
subArr = []
s2_index = 0

for i in s1:
    found = False
    for j in range(s2_index , len(s2)):
        if i == s2[j] :
          sub += i
          found = True
          s2_index += 1
          break
    if found:
        subArr.append(sub)
    else:
        sub = ''

subArr.sort()        
print(subArr)  

sum =int(0)
for i in subArr[len(subArr)-1]:
    sum += ord(i)
print(sum)

