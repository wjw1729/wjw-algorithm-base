
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    def solve():


        for i in range(1,n):
            if a[i]<a[i-1]:
                break
        else:
            print('YES')
            return

        for i in range(1,n):
            if a[i]>a[i-1]:
                break
        else:
            print("YES")
            return

        check=True
        maxn=max(a)
        idx=a.index(maxn)

        for i in range(1,idx):
            if a[i]<a[i-1]:
                check=False
                break

        for i in range(idx+1,n):
            if a[i]>a[i-1]:
                check=False
                break
        if check:
            print('YES')
        else:
            print('NO')
        return

    solve()

