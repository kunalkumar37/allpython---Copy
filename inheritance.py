#inheritance allows us ot define that inherits all the methods and 
#properties from another class


#parent class-- the class being inherited from also callled base class
#child class-- the clss that inherits from another class also called derived class


#create a parent class

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.lastname,self.firstname)

x=Person("john","dor")

x.printname()
"""
here we create a class name person with firstname and lastname properties 
and printname method 

"""

# to create a class that inherits the functionalit form another class send the 
#parent class as a parameter when creating the child class
# here create class named student which will inherit the prooerties 
#and methods from the person class

class Student(Person):
    pass

x = Student("mike","olsen")
x.printname()

#super function that will make the child class inherit all the methods and 
#properties from its parent

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)


