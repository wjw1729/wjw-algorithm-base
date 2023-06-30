from functools import lru_cache
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        mod=10**9+7
        @lru_cache(None)
        def dfs(i,m):
            if m==n-1:
                return 1

            res=0
            for j in range(i,maxValue+1,i):
                res+=dfs(j,m+1)

            return res%mod

        ans=0
        for i in  range(1,maxValue+1):
            ans+=dfs(i,0)
            ans%=mod

        return ans

n=5878
maxva=2900
res=Solution().idealArrays(n,maxva)
print(res)