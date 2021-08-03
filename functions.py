"""
a fucntion is a block of code which only runs when it is called
you can pass daata known as arameters into a fucntion
a fucntion can return data as a result

"""

#function is defined using the def keyword
def my_function():
    print("hello from a fucniton")


#calling a function
def my_function():
    print("hello from a fucttion")

my_function()

#information can be passed into functions as arguments
#specified after the function name under the paranthseis


def my_function(fname):
    print(fname+"refsnes")

my_function("emil")
my_function("emil")
my_function("emil")

my_function("emil")

#fucntions has a number of arguments
def my_function(fname,lname):
    print(fname+" "+lname)

#my_function("emil"+"refsnes")


#what are the *args 
# this means that if u don'nt know how mant arametes that will be passed into 
#your function add a * befor the parameter in afunction 

# by using * the function will recieve a tupel of arguments and can access the items 
def my_function(*kids):
    print("the youngest child is "+kids[2])

my_function("emil","tobais","linus")


#you can also send arguments with the key =value syntax
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#**kwargs
# if u don't lnow how many keyword arguments that will be passed into your function add
#two asterisk ** beforethe parameter name in the function



#there is defaulter parameter in the python 
def my_function(country="norway"):
    print("i am from "+ country)

my_function("sweden")
my_function()


#passing a list as an argument

# the pass statement 
# function definitions cannot be empty but if you for some reason have a fucniton 
#definition with no content put in the pass statemnt to acvoid getting ans error
def my_function():
    pass



# testing the recursion

def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\n recursion examle result")
tri_recursion(6)