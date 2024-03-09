num = int(input("enter ammount: "))

if num == 12000:
    da = num *(10/100)
elif num == 1000:
    da = num *(8/100)
elif num == 8000:
    da = num *(6/100)
elif num == 4000:
    da = num *(4/100)
else:
    da = num *(2/100)

print("da is = " , da)