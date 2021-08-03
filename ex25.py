x="awesome"
def myfunc():
    print("python is "+x)
myfunc()

x="awesome "
def myfunc():
    x="fantastic"
    print("python is "+x)
myfunc()
print("python is "+x)

#use the global keyword the variable belongs ot the global scope
def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is "+x)