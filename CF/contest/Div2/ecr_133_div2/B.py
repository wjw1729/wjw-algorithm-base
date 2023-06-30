
t=int(input())

for _ in range(t):
    n=int(input())
    print(n)
    ans=[]
    a=list(range(1,n+1))
    ans.append(a[:])

    for i in range(1,n):
        a[i],a[i-1]=a[i-1],a[i]

        ans.append(a[:])

    for c in ans:
        print(*c)

