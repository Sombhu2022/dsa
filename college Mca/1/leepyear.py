year = int(input("enter year:"))
if (year%4 == 0 and year%100 != 0) or year %400 ==0:
    print("leepyear")
else:
    print("not")