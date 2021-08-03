import heapq
v=[]
for _ in range(int(input())):
    command=list(map(int,input().split()))
    if command[0]==1:
        heapq.heappush(v,command[1])

    elif command[0]==2:
        v.remove(command[1])
        heapq.heapify(v)


    elif command[0]==3:
        print(v[0])