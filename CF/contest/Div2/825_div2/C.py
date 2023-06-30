

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    a=[a[i]-i for i in range(n)]
    l=0
    r=0
    ans=0
    for l in range(n):
        while r<n and a[r]>=1-l:
            r+=1

        ans+=(r-l)
        #print(l,r)

    print(ans)