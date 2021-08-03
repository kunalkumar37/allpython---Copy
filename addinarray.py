import array as arr

a=arr.array('d',[1.2,2.3,1.3,2.5])

a.append(3.4)
print("array after appendeing",a)

a.extend([223.34,12.23,90.89])
print("array after extending",a)


a.insert(3,9.879)

print("array after isnerting ",a)