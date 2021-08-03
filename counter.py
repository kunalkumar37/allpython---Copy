# the collections module in python provides different types of containers 
# a container is an object that is used to store different objects and provide a way 
#to access the contained objects and iterate over them
"""
counters 
a counter is a sub-class of the dictionary .
it is used to keep the count of the elments in an iterable in the form 
of an unordered dictionary where the key represents the elements in the iterable and value 

"""

# A Python program to show different
# ways to create Counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# with dictionary
#print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
#print(Counter(A=3, B=5, C=2))

# we can form the empty counter in the following manner 




coun=Counter()

coun.update([1,2,3,4,12,3,1,1,1])
print(coun)

# counts can be zero and negative also
c1=Counter(A=4,B=3,C=10)
c2=Counter(A=10,B=3,C=4)
c1.subtract(c2)
print(c1)

