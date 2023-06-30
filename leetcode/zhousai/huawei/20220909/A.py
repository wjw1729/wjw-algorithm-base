from functools import lru_cache
import bisect

a=[int(x) for x in input().split()]
b=int(input())

n=len(a)
a.sort()


@lru_cache(None)
def dfs(t):

    if t==0:
        return [[]]
    idx=bisect.bisect_right(a,t)


    res=None
    maxlen=float('inf')
    for i in range(idx-1,-1,-1):
        tres=dfs(t-a[i])

        if tres!=None:
            tmpl = len(tres[0])

            if tmpl+1<maxlen:
                res=set()
                for x in tres:
                    res.add(tuple(sorted(list(x)+[a[i]])))

                maxlen=tmpl+1
            elif tmpl+1==maxlen:
                for x in tres:
                    res.add(tuple(sorted(list(x)+[a[i]])))


    return list(res) if res else None


ans=dfs(b)
if ans==None:
    print(-1)
else:
    ans.sort()
    for x in ans:
        print(*x)



