# this programs to understand bit wise oparator

# AND - ( & ) --> if two bit are 1 then 1 other wise 0 .
a = 10 & 7
print(a)

# OR - ( | ) --> if minimum one bit is 1 then return 1 , other wise 0 .
b = 10 | 7
print(b)


# NOT - ( ~ ) --> Then first convert binary formate then calculate 1's compliment of this number ... if number is 
#                  nagetive then  calculate 2's compliment and return this ans .
#                  if number is posetive then return this number
c = ~5
print(c)

d = ~-6
print(d)



# XOR - ( ^ ) --> if number of 1's is odd -> 1.
#                 if  number of 1's is even -> 0 . if two bits are 0 then 0 . 

xor = 10 ^ 7
print(xor)



# RIGHT SHIFT - ( >> )   ---> The right shift operator shifts the bits of a
#                     number to the right by a specified number of positions.
#                    Each right shift effectively divides the number by 2 for each shift.


# Example with a number
number = 10        # In binary: 1010
shift_count = 2    # Shift right by 2 positions

result = number >> shift_count

print(result)      # Output: 2 (In binary: 10)


# LEFT SHIFT - ( << ) --> The left shift operator shifts the bits of a number to the 
#                         left by a specified number of positions. 
#                        Each left shift effectively multiplies the number by 2 for each shift.

# Example with a number
number = 10        # In binary: 1010
shift_count = 2    # Shift left by 2 positions

result = number << shift_count

print(result)      # Output: 40 (In binary: 101000)
