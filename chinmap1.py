from collections import ChainMap

a={1:"edureka",2:"neghgo",3:"gnwof"}
b={3:"ml",4:"ai"}

al=ChainMap(a,b)
print(al)