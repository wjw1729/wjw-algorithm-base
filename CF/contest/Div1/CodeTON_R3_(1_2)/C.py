
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in list(input())]
    b=[int(x) for x in list(input())]

    def solve(a,b):
        ans=[]
        if a==b:
            ans.append((0,n-1))
            a=[1-x for  x in a]

        check=all(a[i]+b[i]==1 for i in range(n))
        if not check:
            print('NO')
            return
        cnt1=a.count(1)
        if cnt1%2==1 or cnt1==0:
            for i in range(n):
                if a[i]==1:
                    ans.append((i,i))

            print('YES')
            print(len(ans))
            for x in ans:
                print(*[y+1 for y in x])

        else:
            print('NO')
            return








    solve(a,b)