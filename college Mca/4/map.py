arr= [10 , 20 , 30 ,40 , 50]

tuple = [44 , 55, 66, 77]

dic = {
    "som":20,
    "dip":40
}
def By_10(ele):
    return ele//10

map_function = map(By_10 , arr)
print(list(map_function))