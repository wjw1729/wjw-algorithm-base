
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    ans=a[0]
    for x in sorted(a[1:]):
        if x>ans:
            ans+=(x-ans+1)//2

    print(ans)