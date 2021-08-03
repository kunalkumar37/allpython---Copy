#try block lets you test a block of code for errors
#except block lets u handle the error
# finally block lets you execute code regardless of the result of the try and except blocks
"""try:
    print(x)
except:
    print("an exception occured")

"""
"""try:
    print(x)

except NameError:
    print("variable x is not defined")

except:
    print("something else wen wrong")"""


# we can use as many as exceptions as u want for special error

"""try:
    print(x)
except:
    print("something went wrong")

finally:
    print("the try except is finis"""

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()