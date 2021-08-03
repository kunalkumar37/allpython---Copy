""" 
a default dict is also sub-class to dictionary it is used
to provide some default values for the key that does not exist and never raises a key error 
"""

from collections import defaultdict

d= defaultdict(int)
l=[1,2,3,4,4,6,7,1]
for i in l:
    d[i]=i

print(d)


