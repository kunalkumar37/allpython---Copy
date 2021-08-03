import sys

def powersum(x,n,num):
    value=x-num**n
    if value<0:
        return 0
    elif value==0:
        return 1
    else:
        return powersum(value,n,num+1)+powersum(x,n,num+1)


if __name__=="__main__":
    x=int(input())
    N=int(input())
    result=powersum(x,N,1)
    print(result)