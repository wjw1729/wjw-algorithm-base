from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

t=int(input())

for _ in range(t):
    n=int(input())
    pa=[0]*n
    g=[[] for _ in range(n)]
    a=[0]*n
    b=[0]*n

    for j in range(1,n):
        pj,aj,bj=[int(x) for x  in input().split()]
        pj-=1
        pa[j]=pj
        g[pj].append(j)
        a[j]=aj
        b[j]=bj


    def solve():
        A=[0]*n
        B=[0]*n

        ans=[0]*n

        @bootstrap
        def dfs(u,path,preidx):

            A[u]=A[pa[u]]+a[u]
            B[u]=B[pa[u]]+b[u]

            l=preidx
            r=len(path)-1

            while l<=r:
                mid=(l+r+1)//2
                if B[path[mid]]<=A[u]:
                    l=mid+1
                    ans[u]=mid
                else:
                    r=mid-1


            for v in g[u]:
                path.append(v)
                yield dfs(v,path,ans[u])
                path.pop()

            yield
        dfs(0,[0],0)

        print(*ans[1:])

    solve()


