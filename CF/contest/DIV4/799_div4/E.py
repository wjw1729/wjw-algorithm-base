

t=int(input())

for _ in range(t):
    n,s=[int(x) for x in input().split()]
    a=[int(x) for  x  in input().split()]

    presum=[0]*(n+1)
    index={0:0}

    ans=0
    for i in range(1,n+1):
        presum[i]=presum[i-1]+a[i-1]
        if presum[i]-s in index:
            ans=max(ans,i-index[presum[i]-s])
            #print(i,index[presum[i]-s],'?')

        if presum[i] not in index:
            index[presum[i]]=i

    if ans==0:
        print(-1)
    else:
        print(n-ans)
