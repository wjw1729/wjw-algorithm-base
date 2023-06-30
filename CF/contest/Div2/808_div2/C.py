
t=int(input())
for _ in range(t):
    n,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    def solve():
        vis=['0']*(n)

        c=0
        for i in range(n-1,-1,-1):
            if a[i]>c:
                c+=1

            vis[i]='1'

            if c==q:
                break

        idx=i-1

        for i in range(idx,-1,-1):
            if a[i]<=q:
                vis[i]='1'


        print(''.join(vis))
        return

    solve()

