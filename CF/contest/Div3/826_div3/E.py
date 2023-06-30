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
    b=[int(x) for x in input().split()]

    f={}
    @bootstrap
    def dfs(i,j):
        if i in f:
            yield f[i]

        if b[i]==j-i or  b[j]==j-i:
            f[i]=True
            yield True
        if i+b[i]+1<=j:
            res=yield dfs(i+b[i]+1,j)
            if res:
                f[i]=True
                yield True

        for k in range(i+1,j+1):
            if b[k]==k-i:
                if k+1<j:
                    res=yield dfs(k+1,j)
                    if res:
                        f[i]=True
                        yield True

        yield False


    if  dfs(0,n-1):
        print('YES')
    else:
        print('NO')

