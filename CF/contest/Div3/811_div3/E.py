
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    def solve():
        if any(x%5==0 for  x in a):
            tmp=set()
            for x in a:
                x=x+x%10
                tmp.add(x)

            if len(tmp)==1:
                print('YES')
                return
            else:
                print('NO')
        else:

            vis=[-1]*10

            for c in a:
                b=c%10
                d=c//10
                if d%2==0:
                    if vis[b]==1:
                        print('NO')
                        return
                    vis[b]=0
                else:
                    if vis[b]==0:
                        print('NO')
                        return
                    vis[b]=1

            if (all(vis[i]==0 for i in [1,2,4,8] if vis[i]!=-1) and all(vis[i]==1 for i in [3,6,7,9] if vis[i]!=-1)) or \
                (all(vis[i] == 1 for i in [1, 2, 4, 8] if vis[i] != -1) and all(vis[i] == 0 for i in [3, 6, 7, 9] if vis[i]!=-1)):
                print('YES')
                return
            else:
                print('NO')
                return


    solve()
