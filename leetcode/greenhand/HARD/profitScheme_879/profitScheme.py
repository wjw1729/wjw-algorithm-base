"""
author:wjw
分析：对于小数量的profit的数组，排除子集中不满足profit.minProfit>=minProfit和profit.group<=n的数量。
"""

import itertools


class Solution:
    def profitScheme(self, n, minProfit, group, profit):
        profit_len = len(profit)

        subset = []
        for i in range(1, profit_len + 1):
            subset += set(itertools.combinations(range(profit_len), i))

        ans = 0
        subset_len = len(subset)
        for i in range(subset_len):
            select = subset[i]
            human_total = 0
            sl_minprofit = 0
            for s in select:
                human_total += group[s]
                sl_minprofit +=profit[s]

            if human_total <= n and sl_minprofit >= minProfit:
                ans += 1

        return ans


n = 5
minProfit = 3
group = [2, 2]
profit = [2, 3]
res = Solution().profitScheme(n, minProfit, group, profit)
print(res)
