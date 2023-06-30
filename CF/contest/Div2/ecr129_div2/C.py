

def minmoves(a,b):

    pls=[(a[i],b[i],i+1) for i in range(n) ]
    pls.sort()

    for i in range(1,n):
        if pls[i][1]<pls[i-1][1]:
            return -1,None

    ans=[]

    cls=list(range(1,n+1))
    hmap={i:i-1 for i in range(1,n+1)}

    for i in range(n):
        c=pls[i][2]

        if c==cls[i]:
            continue
        else:
            ans.append((i+1,hmap[c]+1))

            ci=cls[i]

            cls[i],cls[hmap[c]]=c,cls[i]
            hmap[ci],hmap[c]=hmap[c],hmap[ci]


    return len(ans),ans











t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    res=minmoves(a,b)
    if res[0]==-1:
        print(-1)
    else:
        print(res[0])
        for i in res[1]:
            print(*i)
