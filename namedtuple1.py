from collections import namedtuple
a = namedtuple('courses','name , technology')
s=a("data science","python")

d=a._make(["artificial intelligence", "phthon"])

print(d)
print(s)