from  collections import Counter
a=[1,1,2,3,2,2,4,4,3,3]

c=Counter(a)

print(c)

print(list(c.elements()))


print(c.most_common())

sub={2:1,4:2}

print(c.subtract(sub))

print(c.most_common())