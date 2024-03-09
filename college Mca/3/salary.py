n = int(input("enter the basic salary: "))

if n <5000:
    da = n*70/100
    hra = n* 10/100
else:
    da = n * 75/100
    hra = n + 1000
total = n + da + hra
print(total , da , hra , n)
    