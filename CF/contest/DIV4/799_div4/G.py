

t=int(input())
for _ in range(t):
    n,k=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]


    tag=[0]*n
    for i in range(n-1):
        if a[i]<2*a[i+1]:
            tag[i]=1

    tagsum = [0] * (n + 1)
    for i in range(1,n+1):
        tagsum[i]=tagsum[i-1]+tag[i-1]


    def check(i):
        if tagsum[i+k]-tagsum[i]==k:
            return True
        return  False

    ans=0
    l=0
    while l<=n-k-1:
        while l<=n-k-1 and not check(l):
            l+=1

        r=l
        while r<=n-k-1 and check(r):
            r+=1

        ans+=r-l
        l=r



    print(ans)




