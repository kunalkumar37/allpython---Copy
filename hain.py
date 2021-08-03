""" 
a chainmap encapsulates many dictionaries into a single unit and returns
 a list in dictionaries

"""

from collections import ChainMap

d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}

c=ChainMap(d1,d2,d3)

print(c)

"""

values form chainmpa can be accesed uisng key name 
they can be accessed by using the keys() and values( ) method

"""
# accessing the value using keyname

print(c['a'])

print(c.values())

# we can add dictionary by using new_child() method 
# the newly added dictionary is added at the beginning of the chinmap

chain=ChainMap(d1,d2,d3)

print("all the chainmap content are:")
print(chain)

