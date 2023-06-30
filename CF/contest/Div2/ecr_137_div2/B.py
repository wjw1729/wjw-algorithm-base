t=int(input())
for _ in range(t):
    n=int(input())

    if n%2==1:
        a=[]
        b=[]
        for i in range(1,n//2+2):
            a.append(i)
        for i in range(n//2+2,n+1):
            b.append(i)

        ans=[]
        for i in range(len(a)):
            ans.append(a[i])
            if i<len(b):
                ans.append(b[i])
    else:
        a=[]
        b=[]

        for i in range(1,n//2+1):
            a.append(i)

        for i in range(n//2+1,n+1):
            b.append(i)

        ans=[]
        for i in range(len(a)):
            ans.append(b[i])
            ans.append(a[i])

    print(*ans)