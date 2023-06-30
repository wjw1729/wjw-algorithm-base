


t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    check=True
    end=False
    presum=[0]*(n+1)
    for i in range(1,n+1):
        presum[i]=presum[i-1]+a[i-1]
        if presum[i]==0:
            end=True
        if not end:
            if  i<n and presum[i]<=0:
                check=False
                break
        else:
            if presum[i]!=0:
                check=False
                break
        if i==n and presum[i]!=0:
            check=False
            break


    if check:
        print('YES')
    else:
        print('NO')


