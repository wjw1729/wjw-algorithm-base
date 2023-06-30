"""
author:wjw
分析：由于要求的是最大数量，捡便宜的买就行了
"""


class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        sum = 0
        ans = 0
        for i in range(len(costs)):
            sum += costs[i]

            if sum > coins:
                return ans
            ans += 1

        return ans


costs = [1,6,3,1,2,5]
coins = 20
res = Solution().maxIceCream(costs, coins)
print(res)
