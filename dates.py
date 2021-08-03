#a date in python is not a data type of its own but we can import a module named datetime ot work with dates as date objects

import datetime
x=datetime.datetime.now()

print(x)

print(x.year)
print(x.strftime("%A"))

x=datetime.datetime(2020,5,17,12,2,56)
print(x)

#strftime() method 
x=datetime.datetime(2002,1,24)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%a"))
