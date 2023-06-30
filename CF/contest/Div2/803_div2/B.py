

t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]


    if k==1:
        print(n//2 if n%2==1 else (n-1)//2)

    else:
        ans=0
        for i in range(1,n-1):
            if a[i]>a[i-1]+a[i+1]:
                ans+=1

        print(ans)
