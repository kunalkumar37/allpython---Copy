#an iterator is an object that contains a countable number of values
# an interator is an object that can be iterated upon, meanong that u can traverse thor
#OUGH ALL the values


# lists, tuples dictionaries and sets are all iterable objects 


# an iterator is an object which implements the iterator protocol 
#which consits __iter__() and __next__()
mytuple=("apple","banana","cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr="bananana"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print(next(myit))
print(next(myit))
print(next(myit))


mytuple=("apple", "banana", "cherry")

for x in mytuple:
    print(x)



class Mynumbers:
    def __iter__(self):
        self.a=1;
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass = Mynumbers()

myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# __iter__() method acts similar you can do operaatins but must always return
# the iterator object itself

#__next__() method also allows you to do operations and must return the next item 
#in the sequence
