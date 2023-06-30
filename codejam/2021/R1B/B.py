from collections import defaultdict
def create(x,amount,a,b):

    h=defaultdict(int)
    h[x]=1


    while 1 :

        for k,v in sorted(h.items(),key=lambda x:x[0]):

            if k-a>0:
                h[k-a]+=v
            if k-b>0:
                h[k-b]+=v

            h[k] = 0
            del h[k]


        for i in range(n):
            if i+1 in h:
                minv=min(h[i+1],amount[i])
                amount[i]-=minv
                h[i+1]-=minv
                if h[i+1]==0:
                    del h[i+1]

        if all(x==0 for x  in amount):
            return True

        if h=={} or all(x<=a for x in h.keys()):
            break


    return False





def minmetal(amount,a,b):

    for i in range(n+1,403):
        if create(i,amount[:],a,b):
            return i

    return -1


t=int(input())
for i in range(t):
    n,a,b=[int(x) for x in input().split()]
    amount=[int(x) for x in input().split()]
    res=minmetal(amount,a,b)
    if res!=-1:
        print('Case #%d: %d'%(i+1,res))
    else:
        print('Case #%d: %s'%(i+1,'IMPOSSIBLE'))
