from array import *
num=array("i",[1,2,4,5,6,7])
num.insert(2,3)
print(num)

print(num.pop(4))
print(num)

num.reverse()
print(num)

num.remove(4)
print(num)

for x in num:
    print(x)
