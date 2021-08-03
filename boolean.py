#boolean represnet one of two values::
#true false
print(bool("hello"))

print(bool(14))

class myclass():
    def __len__(self):
        return 0

myobj=myclass()
print(bool(myobj))

def myfunction():
    return True
print(myfunction())

def myfunction():
    return True
if myfunction():
    print("yes")
else:
    print("no")

#isinstance() function which can be uesd ot determine if an objedt is of certain type
x=200
print(isinstance(x,int))

print(10+5)

print(10//5)
print(10/5)

#membership operator
#in  returns True if a sequence with the specified value is present in the object
#not in returns true if a sequence woth the spefified value is not present in the object
#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off