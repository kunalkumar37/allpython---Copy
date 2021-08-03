# an ordereddict is also a sub class of dictinary but unlike dictionary it 
# remembers the order in which the keys were inserted
from collections import OrderedDict
print("this is dict\n")

d={}
d['a']=1
d['c']=2
d['b']=2
d['e']=2


for key,value in d.items():
    print(key,value)
# while deleting and reinerting the same key will push the key to the last ot maitain 
#the order  of insertion of the key


od= OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

print("before deleting")

for key,value in od.items():
    print(key,value)


#deleting element
od.pop('a')

od['a']=1
# reinseting the same
print("\n after reinserting")
for key,value in od.items():
    print(key,value)
    