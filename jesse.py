from heapq import heappop,heappush,heapify
firstline = [int(x) for x in input().split()]
cookies = [int(x) for x in input().split()]

cookieCount = int(firstline[0])
minsweetness = int(firstline[1])

heapify(cookies)

fc=0
try:
    while cookies[0]<minsweetness:
        fc+=1
        c1=heappop(cookies)
        c2=heappop(cookies)
        newcookies=(1*c1)+(2*c2)
        heappush(cookies,newcookies)

    print(fc)

except:
    print("-1")