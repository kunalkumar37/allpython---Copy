# a regex or regular expressons is a sequence of charcters that forms a seaarch pattern

# a regex can be used ot check if astring contains the specified search pattern
import re

txt="the rain in spain"
x=re.search("^the.*spain$",txt)
print(x)
x= re.findall("ai",txt)
print(x)

"""" findall ->>>>returns a list containning all matches
search returns a match object if there isa match anywhere in the string 
split  returns a list where the stirng has been slit at each match 
sub replaces one or many mathces with a string """

x=re.sub("\s",'9',txt)
print(x)
x=re.sub("\s","9",txt,2)
print(x)