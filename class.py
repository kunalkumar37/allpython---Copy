#python is an object oriented programming language
#almost everything in python is object

class Myclass:
    x=5

p1=Myclass()
print(p1.x)

# the real meaning of classes we have ot underastand the built int __init__()
#function
# all classes have a fucntion called __int__() which is always executed when 
#is being intiated

"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person(36,"john")

print(" the name of the person is ::",p1.name)
print("the age of the person is ::",p1.age)"""

# the __init__() fucntion is called automatically every tiem the class is being uesd to create a new objec

# objects can also contain methods methods in objects are functioins that belong ot the object

"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def myfunc(self):
            print("hello my name is "+self.name)
p1=Person("jhon",36)
p1.myfunc()
"""
#the self parameter is a refrence ot the current instance of the class and is used ot 
# access variables that belongs ot the class


class Person:
    def __int__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def myfunc(abc):
        print("hello my name is"+abc.name)

p1=Person("john",36)
p1.myfunc()

p1.age=40# we can modifythe objecct properties

#delete properties on objects by using the del keyword
del p1.age


# we can delete objects using the del keyword 
del p1


# class definitions cannot be empty but if you for some reason have a class 
#definition with no content 
# use the pass staatement to avoid getting error

class Girl:
    pass