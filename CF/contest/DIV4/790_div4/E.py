import bisect



t=int(input())
for _ in range(t):
    n,k=[int(x) for x  in input().split()]
    a=[int(x) for x in input().split()]
    a.sort(reverse=True)
    presum=[0]*(n+1)
    for i in range(1,n+1):
        presum [i]=presum[i-1]+a[i-1]


    for _ in range(k):
        y=int(input())
        if y>presum[-1]:
            print(-1)
        else:
            idx=bisect.bisect_left(presum,y)
            print(idx)






