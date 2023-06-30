
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    tt=sum(a)
    ans=n
    for i in range(2,n+1):
        if tt%i==0:
            targ=tt//i
            tmp=0
            cnt=0
            cnt1=0
            check=True
            for i in range(n):
                if cnt+a[i]>targ:
                    check=False
                    break

                cnt+=a[i]
                cnt1+=1
                if cnt==targ:
                    tmp=max(tmp,cnt1)
                    cnt=0
                    cnt1=0
            if check:
                ans=min(ans,tmp)

    print(ans)







