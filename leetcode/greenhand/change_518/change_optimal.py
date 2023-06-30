"""
author:other
分析：实际上这里的状态转移公式为dp[i][j]=dp[i-1][j]+dp[i][j-coin]。所以第二层循环可以正向开始，且不用考虑当前coin的数量。
"""


class Solution:
    def change(self, amount, coins):

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin]

        return dp[-1]


amount = 5
coins = [1, 2, 5]
res = Solution().change(amount, coins)
print(res)
