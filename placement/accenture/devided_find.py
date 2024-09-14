# given divideds a int array and , three input d , q , r .. divided = (p*q)+r ,
#  if divided presents in array then return location , otherwise -1.

d = 3
q = 5
r =2
arr = [5 , 6 ,7 , 17 , 32 , 34]

div = (d*q)+r

print(arr.index(div))
