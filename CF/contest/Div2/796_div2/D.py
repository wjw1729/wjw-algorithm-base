def maxnum(a):

    if k<=n:
        presum=[0]*(n+1)
        for i in range(1,n+1):
            presum[i]=presum[i-1]+a[i-1]

        ans=0
        for i in range(n-k+1):
            ans=max(ans,presum[i+k]-presum[i])

        ans+=(k-1)*k//2




    else:
        ans=sum(a)

        #tt=n-((k-1)%n)
        res=(k-1)*n-(n-1)*n//2

        ans+=res




    return ans
t=int(input())
for _ in range(t):
    n,k=[int(x) for x  in input().split()]
    a=[int(x) for  x in input().split()]

    res=maxnum(a)
    print(res)