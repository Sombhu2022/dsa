
def fun(str , n , ch1 , ch2):
    if str == "" or str == " ":
        return "null"
    str_list = list(str)
    print(str_list)
    for i in range(n):
        if str_list[i].lower() == ch1:
            str_list[i] = ch2
        elif str_list[i].lower() == ch2:
            str_list[i] = ch1
    return ''.join(str_list).lower()

str = 'sombhu das '
ch1 = 'm'
ch2 = 'd'
n = len(str)

res = fun(str , n , ch1 , ch2)
print(res)

