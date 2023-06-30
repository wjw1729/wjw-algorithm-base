t=int(input())

for _ in range(t):
    n=int(input())
    if n%2==0:
        a=list(range(n//2,0,-1))
        b=list(range(n,n//2,-1))
        ans=[]
        for i in range(n//2):
            ans.append(a[i])
            ans.append(b[i])

    else:
        a = list(range(n // 2+1, 0, -1))
        b = list(range(n, n // 2+1, -1))

        ans = []
        for i in range(n // 2+1):
            ans.append(a[i])
            if i<len(b):
                ans.append(b[i])

    print(*ans)

