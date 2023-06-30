"""
author:wjw
分析：贪心算法  or dp?区别？dp[i]表示总金i的最小硬币数。
        动态规划
"""

import bisect


class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        x = float('inf')
        dp = [x] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            if i < coins[0]:
                continue

            if i in coins:
                dp[i] = 1
                continue
            max_coins_index = bisect.bisect_left(coins, i)
            for j in range(max_coins_index):
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[amount] if dp[amount] != x else -1


coins = [2]
coins = [1]
amount = 2
res = Solution().coinChange(coins, amount)
print(res)
