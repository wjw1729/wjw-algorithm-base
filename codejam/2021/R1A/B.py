from functools import lru_cache
import math


def maxscore(prime,amount):

    maxp=max(prime)
    n=sum(amount)
    maxnum2=math.ceil(math.log2(maxp*n))

    sum2=maxnum2*maxp

    total=sum(prime[i]*amount[i] for i in range(len(prime)))


    for eq in range(total,max(total-sum2-1,0),-1):
        cnt=[]
        eqnum=eq
        if eq==25:
            pass
        for p in prime:
            cntt=0
            while eqnum%p==0:
                cntt+=1
                eqnum//=p
            cnt.append(cntt)

        if any(cnt[i]>amount[i] for i in range(m)) or eqnum !=1:
            continue

        tmp=sum([prime[i]*(amount[i]-cnt[i])  for i in range(m)])
        if tmp==eq:
            return tmp

    return 0

t=int(input())
for i in range(t):
    m=int(input())
    prime=[]
    amount=[]
    for _ in range(m):
        p,n=[int(x) for x in input().split()]
        prime.append(p)
        amount.append(n)

    res=maxscore(prime,amount)
    print('Case #%d: %d'%(i+1,res))