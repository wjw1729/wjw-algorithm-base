


def mincantbuy(a,b):

    if a==0:
        return 1
    return a+2*b+1


t=int(input())
for _ in range(t):
    a,b=[int(x) for x in input().split()]

    print(mincantbuy(a,b))





