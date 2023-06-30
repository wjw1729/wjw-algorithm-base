from functools import lru_cache
def minops(x):


    @lru_cache(None)
    def solve(x):
        if x>=10**(n-1):
            return 0
        numset=set(str(x))


        res=float('inf')
        for i in numset:
            i=int(i)
            if i in [0,1]:
                continue
            res=min(res,solve(x*i)+1)

        return res


    ans=solve(x)
    return  ans if ans!=float('inf')  else -1



n,x=[int(x) for x in input().split()]
check=True
ans=0
print(minops(x))