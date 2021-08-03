from collections import deque

a=['e','d','u','r','e','k','a']
d=deque(a)
print(d)


d.append("kunal kumar")
print(d)

d.appendleft("kumar kunal")
print(d)

d.pop()
print(d)

d.popleft()
print(d)

