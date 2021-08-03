mylist=["apple","banana",'cherry']
print(mylist)

# there are 4 built in data tye in python used ot store collections of data 
# these are lists, tupels, set,dictionaary
print(mylist[0])

print(len(mylist))

mylist1=["abdbwo",34,True, 40,"Male"]
print(mylist1)

print(type(mylist1))

#we can use list constructor to make another list
thislist=list(("apple","banana","cherry","guava","hajmola"))

print(thislist)

print(mylist[2:5])# this search will start at index 2 (included) and end at index 5(not included)
#first item has index 0

# we cna modify the item value 
thislist=["apple","banana","cherry"]
thislist[1]="blackcurrant"
print(thislist)

# we can change the range of item value in the list


thislist=["apple","banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:4]=["fwonwlf","lngwowfnow"]
print(thislist)

# the lenght of the list will change whn the nmber of items insertd does not match the number of items replaced 


#insert items 
# to insert a new item without replacing any of the existing value we can use the insert() method


thislist=["apple", "banana", "cherry"]

thislist.insert(2,"knalnan")

print(thislist)# the size of the list is change


#append fucntion isnert the elment in the last
thislist=["apple", "banana", "cherry"]

thislist.append("orange")
print(thislist)

#to append elements from another list ot the current lost use the extend() function

thislist=["apple","banana","cherry"]
tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

#remove method removes the secified item
thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)

#if the index is not specified in the pop fucntion the it remove s the last item

#del keyword also removes the specified index

thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)

#clear() method empties the list
thislist=["aple","nojs","ngwoj"]
#thislist.clear()
print(thislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])#0,1,2



# while loop in python
thislist=["apple", "banana", "cherry","apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1

thislist=["apple", "banana", "cherry"]
#list comprehension offers the shortest syntax for looping thorough lists

[print(x) for x in thislist]

thislist=["orenge","mango","kiwi","pineapple","banana"]
thislist.sort()# sort() method that will sort the list alphanumerically ascending
print(thislist)


thislist=["orenge","mango","kiwi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)


# you can also customize your own fucnion by using the keyboard argument
# sort the list basaed on how close the number is to 50
def myfunc(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

#by default the sort() method is casae sensitive resulting in all capital
#letters being sortd before lower case letters

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
thislist.sort(key= str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()# reverse method use to reverse the list 
print(thislist)


#to make copy of the list
#by using built in list method copy()


thislist = ["apple", "banana", "cherry"]
mylist=thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist=list(thislist)
print(mylist)

#joining of two lists

list1=['a','b','c']
list2 = [1, 2, 3]

list3=list1+list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
# by appending all the elements from the list2 into list1
for x in list2:
    list1.append(x)
print(list1)

"""


Python - List Methods
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""