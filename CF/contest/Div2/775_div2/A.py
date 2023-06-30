
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]
    ans=n-1

    l=0
    while l+1<n and a[l+1]==1:
        l+=1

    r=n-1
    while r-1>=0 and a[r-1]==1:
        r-=1
    if r<l:
        ans=0
    else:
        ans=min(ans,r-l)

    print(ans)



