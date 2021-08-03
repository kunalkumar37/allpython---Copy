# file handling is an important part of any web applications

# file handling
f=open("demofile.txt")

f=open("demofile.txt","rt")

f = open("demofile.txt", "r")
print(f.read(5))

# to delete the file u must import os module
import os
os.remove()

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")

else:
    print("the file does not exist")

import os
os.rmdir("myfolder")  # by using this fucntion we can remove the empty folders
