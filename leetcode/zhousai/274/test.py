from functools import lru_cache

class Solution:
    def largestNumber(self, cost, target: int) -> str:

        cost_pair = [(cost[i], i + 1) for i in range(9)]

        cost_pair.sort(key=lambda x: (x[0], -x[1]))

        @lru_cache(None)
        def solve(target):
            if target == 0:
                return ''

            res = 0
            check = False
            for c, num in cost_pair:
                if c > target:
                    continue
                if solve(target - c) == None:
                    continue
                res = max(res, int(str(num) + solve(target - c)))
                check = True
            if not check:
                return None

            return str(res)

        ans = solve(target)
        return ans if ans != None else '0'

cost=[5,4,4,5,5,5,5,5,5]
target=19
res=Solution().largestNumber(cost,target)
print(res)