# string format()--the format method allows you to format selcted parts of a string

price = 49
txt="the price is {} dollara"

print(txt.format(price))

quantity =3
itemno = 567
price = 49
myorder=" i want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity,itemno,price))


age= 36
name="jhon"
txt="his name is {1}.{1} is {0} years old"
print(txt.format(age,name))

myorder="i have a {carname}, it is a {model}"
print(myorder.format(carname="ford",model="mustang"))