str = str(input("enter the word = "))

upper_count = 0
lower_count = 0

for i in range(len(str)):
    if str[i] == str[i].upper():
        upper_count +=1
    elif str[i] == str[i].lower():
        lower_count +=1

if lower_count > upper_count:
    print(str.lower())
else:
    print(str.upper())