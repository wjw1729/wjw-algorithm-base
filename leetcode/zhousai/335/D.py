from functools import lru_cache
class Solution:
    def waysToReachTarget(self, target: int, types) -> int:

        mod=10**9+7

        @lru_cache(None)
        def solve(t,i):
            if t==0:
                return 1
            else:
                if i>=len(types):
                    return 0

            ans=0
            for j in range(types[i][0]+1):
                if t-j*types[i][1]<0:
                    break
                ans+=solve(t-j*types[i][1],i+1)
                ans%=mod

            return ans

        return solve(target,0)

target = 6
types = [[6,1],[3,2],[2,3]]

res=Solution().waysToReachTarget(target,types)
print(res)
