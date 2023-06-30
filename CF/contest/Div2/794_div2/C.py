




t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    if n%2==1:
        print('NO')
    else:
        a.sort()
        ans=[]
        b1=a[:n//2]
        b2=a[n//2:]
        check=True
        for i in range(n//2):
            if b2[i]<=b1[i] or (i<n//2-1 and b2[i]<=b1[i+1]):
                check=False
                break
            ans.append(b1[i])
            ans.append(b2[i])

        if not check:
            print('NO')
        else:
            print('YES')
            print(*ans)