

t=int(input())
for _ in range(t):
    n,k=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]

    ans=0

    b=[0]*k
    for i in range(n):
        ans+=a[i]//k
        b[a[i]%k]+=1

    j=0
    res=0
    while j<k:
        if j==k-j:
            ans+=res//2
            break
        tmp=min(res,b[j])
        res-=tmp
        b[j]-=tmp
        ans+=tmp


        j+=1
        if j<=k-j:
            res+=b[k-j]
        else:
            ans+=res//2
            break


    print(ans)


