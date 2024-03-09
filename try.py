# a = [0, 1, 2, 3]
# for a[0] in a:
#     print(a[0])
#     print(a[1])
# print("a 0" , a)


# a = [0, 1, 2, 3]
# i = -2
# for i not in a:
#     print(i)
#     i += 1


# example = "snow world"
# example[3] = 's'
# print(example)

print("ccdcddcd".find("c"))


# n = input("enter numbers")
# l=list(n)

# x ="abcdefi"
# while "i" in x:
#     print("0o", end=" ")
    
x = 'abcd'
for i in x:
    # print(i)
    print(i.upper())
print(x)

y = 'abcd'
for i in range(len(y)):
    print(i)
    # print(i.upper())

# x = 'abcd'
# for i in range(len(x)):
# x = 'a'
# print(x)

x = (2+4.00,2**4.000)
print(x)

x=4+3%5
print(x)

for i in range(10):
    if i == 5:
        break
    else:
        print(i)
else:
    print("Here")
string = "my name is x"
for i in string:
    print(i , end=",")

a = [0, 1, 2, 3]
for a[0] in a:
    print(a[0])

# example = "snow world"
# example[3] = 's'
# print(example)

def func(n):
    if(n==1):
        return 1
    else:
        return(n+func(n-1))
print("ans",func(4))

print("ccdcddcd".find("d"))

print(round(4.576))
print('2'==2)

z = "xyz"
j = "j"
while j in z:
    print(j, end=" ")
print('o')

d = {0: 'a', 1: 'b', 2: 'c'}
for j,i in d.items():
    print(i)
    
d = {0, 1, 2}
for x in d: print(x)
print("end")

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

x = "abcdef"
# i = "a"
while i in x:
    print(i, end = " ")
    

x = 'abcd'
for i in x:
    print(i)
    x.upper()

x = 'abcd'
for i in x:
    print(i.upper())

# x = 'abcd'
# for i in range(x):
#     print(i)

# x = 'abcd'
# for i in range(len(x)):
#     print(i.upper())

# for i in range(2.0):
#     print(i)

for i in range(0):
    print(i)
    
x = 'abcd'
for i in range(len(x)):
    x = 'a'
    print(x)
    
x = 'abcd'
for i in range(len(x)):
    x[i].upper()
print (x)