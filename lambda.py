# a lambda fucntion is a small anonymous fucntion
# a lambda function can take any number of arguments but can only have one expressions
# lambda arguments : expression

x= lambda a:a+10
print(x(5))
# add 10 to argument a, and return the result

#lambda functions can take any number of arguments
x=lambda a,b:a*b
print(x(5,6))


x= lambda a,b,c: a+b+c
print(x(5,6,2))

def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11))
print(mytripler(11))