def fan(n):
    if n == 0:
        return 0
    else: fan(n-1)
    print(n)

print(fan(10))
print("ok")

ans =0
jewels ='aA'
stones ='aAAuta'
for i in jewels:
    if i in stones:
        print(i)
        ans += stones.count(i)
print(ans)