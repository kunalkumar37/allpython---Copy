import array as arr
a=arr.array('d',[1,2,3,4])

print(a[:-3])
print(a[0:3])
#this ::-1 doesn't rint the reverse of the array but it print the reverse copy of the array

print(a[::-1])