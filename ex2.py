x="aweosme "
def myfunc():
    global x
    x="fantastic"
myfunc()
print("ython is "+x)

x=memoryview(bytes(789))
print(x)
print(type(x))

x=bytearray(5)
print(x)
print(type(x))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x=35e3
y=12e4
z=-87.7e100
print(z)
print(y)
print(x)


#python does not have a random() function but python has a built in module callled random that 
#can be used to make random numbers

import random
print(random.randrange(1,10))