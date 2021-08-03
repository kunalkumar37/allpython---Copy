from sys import stdin
from heapq import heappop,heappush

heap=[]
item_lookup=set()

def push(v):
    heappush(heap,v)
    item_lookup.add(v)


def delete(v):
    item_lookup.delete(v)

def print_min():
    while heap[0] not in item_lookup:
        heappop(heap)

    print heap[0]


cmds={
    1:push,
    2:delete,
    3:print_min
}


n=int(stdin.readline())
for _ in range(n):
    data=map(int,stdin.readline().split(" "))
    cmds[data[0]](*data[1:])




