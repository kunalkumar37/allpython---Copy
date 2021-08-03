#multiline strings are """
# """ or three single quote'''
#'''

a="hello world "
print(a[1])


for x in "banana":
    print(x)

a="hello world "
print(len(a))


# to check if a certain phrase or character is present in a string we can use the keyboard 
# in
txt="the best things in life aare freee!!!"
print("free " in txt)


# use it in an if statemnet 
txt="the best things in life are free!!!"
if "!!!!" in txt:
    print("yes , free is present ")
else:
    print("no prsent in the sting")


#check if not certain chaaracter jor phrase in a string 
#using not in
txt="the best things in life are free!!"
if "expensive" not in txt:
    print("expensive is not present" )


a="kunal is a good boy"
print(a.upper())

b="kunal is GOOD PROGRAMMER"
print(b.lower())

#remove whitespace 
#strip() fucntions remove any whitespace  from the beginning and the end
a=" hello, world "
print(a.strip())


#replace("h","j")  replcaes the h with j 
a="hello world"
print(a.replace("h",'j'))

#split string 
#split() method returns a list where the text between the specified separator the list items
#split() method splits the string into substring if it finds instance s of the separaot
a="hello, world, is, a ,first, line, of ,every, programmer"
print(a.split(","))


age=36
#txt="my name is john , i am " + age
print(txt)

#as till now we have learnt we cannot combine string and integer at a time
#but we can combine using format ( ) mathod 
age=36
txt="my name is john , and i am {}"
print(txt.format(age))
#the formaat () method takes unlimited number of arguments and are placed into the respective placeholders
quantity=3
itemno=567
price=49.95
myorder="i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))
#we can use indexes also


# to insert characters that are illegal in a strings use an escape character
#escape character \
#you are not allowed to use double quotes inside the another double quotes
txt="we are the so-called \"vikings\" from the north"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

txt = "\110\145\154\154\157"
print(txt) 

txt="hello \bworld!!!"
print(txt)

#python has a set of built in methods that you can use on strings
#all strings methods returns new values they don not change the original string 


