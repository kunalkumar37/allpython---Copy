import array as arr
a=arr.array('f',[1,2,3,4,5,6])
print("popping last element from the array is",a.pop())
print("popping the 4th elemnet from the array is ",a.pop(3))

a.remove(3)
print("after using rmove function to remove the 3 is ",a)