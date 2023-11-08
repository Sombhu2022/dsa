n=int(input("enter the range:"))
print("enter array")
ans=[]
def fun(i):
    if i == 1:
        return 1

    return i*fun(i-1)




# for i in range(1,n+1,1):
#     fact=fun(i)
#     if fact>n:
#         break
#     ans.append(fact)
# print(ans)