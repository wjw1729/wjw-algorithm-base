t=int(input())

for _ in range(t):
    n=int(input())
    h=[int(x) for x in input().split()]


    a1=[]
    for i in range(1,n-1,2):
        if h[i] <= h[i - 1] or h[i] <= h[i + 1]:
            a1.append(max(h[i-1]+1,h[i+1]+1)-h[i])
        else:
            a1.append(0)

    ans=sum(a1)

    if len(h)%2==0:
        a2=[]
        for i in range(2,n-1,2):
            if h[i] <= h[i - 1] or h[i] <= h[i + 1]:
                a2.append( max(h[i - 1] + 1, h[i + 1] + 1) - h[i])
            else:
                a2.append(0)

        n=len(a1)
        presum1=[0]*(n+1)
        for i in range(1,n+1):
            presum1[i]=presum1[i-1]+a1[i-1]

        presum2=[0]*(n+1)
        for i in range(1,n+1):
            presum2[i]=presum2[i-1]+a2[i-1]

        for i in range(n+1):
            ans=min(ans,presum1[i]-presum2[i]+presum2[-1])




    print(ans)

