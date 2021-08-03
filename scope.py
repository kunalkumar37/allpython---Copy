# a vriable is only avaible from inside the region it is created thids is caclled scope

# a varible created inside a function belongs to the local scope of that funcion and 
#can only be used inside that function

def myfunc():
    x=500
    print(x)


myfunc()
# in the upper case the varible x is not avaible for outside the fucntion 
#but it is avaible for fucntion inside the other function 
def myfun():
    x=522
    def myinnerfunc():
        print(x)

    myinnerfunc()

myfunc()

#global scope is a varible creaated in the main body of the python code is 
#a gobal varible andbelongs to the global scope


x=300

def myfunc():
    print(x)

myfunc()

print(x)


# an important case in which the python understand that the there are two varible 

def myfunc():
    x=500
    print(x)

myfunc()
print(x)


#global keyboard create a global varible but are stuck in the local scope u can use 
# the global keyword 
def myfunc():
    global x
    x=456

myfunc()
print(x)

