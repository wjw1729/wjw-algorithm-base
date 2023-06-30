"""
author:wjw
分析：dp[i][j]表示到i-1个coins时，总和为[j]时的总数量。

"""


class Solution:
    def change(self, amount, coins):
        n = len(coins)
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(amount, -1, -1):
                m = j // coins[i - 1]
                for k in range(1, m + 1):
                    dp[j] += dp[j - coins[i - 1] * k]

        return dp[amount]


amount = 0
coins = [10]
res = Solution().change(amount, coins)
print(res)
