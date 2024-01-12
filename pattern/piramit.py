    #    1
    #   2 3
    #  4 5 6
    # 7 8 9 10


n=4
print(n)
number=1
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(1,i+1):
        print(number, end=" ")
        number=number+1
    print()
    
    
    
# rows=5
# number=0
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end=" ")

#         # Print numbers
#     for k in range(1, i + 1):
#         print(number, end=" ")
#         number += 1

#         # Move to the next line after each row
#     print()

