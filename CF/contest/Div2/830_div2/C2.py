import bisect
t=int(input())

for _ in range(t):
    n,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    p = []
    for i in range(n):
        if a[i]:
            p.append(i)

    m=len(p)

    presum=[0]*(m+1)
    xum=[0]*(m+1)

    for i in range(1,m+1):
        presum[i]=presum[i-1]+a[p[i-1]]
        xum[i]=xum[i-1]^a[p[i-1]]


    ans=[]
    for _ in range(q):
        L,R=[int(x) for x in input().split()]
        L-=1
        u,v=L,R
        l=bisect.bisect_left(p,L)
        r=bisect.bisect_left(p,R)

        val=presum[r]-presum[l]-(xum[r]^xum[l])

        if val!=0:
            v=u+1

        x=l
        while x<=min(r,l+31):
            y=max(x+1,r-31)
            while y<=r:
                cur=presum[y]-presum[x]-(xum[y]^xum[x])
                if cur==val:
                    l=p[x]
                    r=p[y-1]+1
                    if r-l<v-u:
                        u=l
                        v=r
                y+=1
            x+=1
        ans.append((u+1,v))


    for a in ans:

        print(a[0],a[1])









