

def minfault(a,b):
    ans=min(abs(a[0]-b[0])+abs(a[-1]-b[-1]),abs(a[0]-b[-1])+abs(a[-1]-b[0]))

    n=len(a)
    res=[]
    for num in [a[0],a[-1]]:
        tmp=float('inf')
        for bi in b:
            tmp=min(tmp,abs(num-bi))
        res.append(tmp)

    for num in [b[0],b[-1]]:
        tmp=float('inf')
        for ai in a:
            tmp=min(tmp,abs(num-ai))
        res.append(tmp)

    ans=min(ans,abs(a[0]-b[0])+res[1]+res[3],abs(a[0]-b[-1])+res[1]+res[2],abs(a[-1]-b[0])+res[0]+res[3],abs(a[-1]-b[-1])+res[0]+res[2],sum(res))



    return ans

t=int(input())

for _ in range(t):
    _=input()
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    print(minfault(a,b))