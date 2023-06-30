"""
author:off
分析:调换了两层循环的顺序，减少了条件判断，不过也没有快很多
"""

import time
class Solution:
    def coinChange(self, coins, amount):
        x = float('inf')
        dp = [x] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != x else -1


t1=time.time()
coins = [1, 2, 5]
amount = 11
coins=[411,412,413,414,415,416,417,418,419,420,421,422]
amount = 9864
res = Solution().coinChange(coins, amount)
print(res)
print(time.time()-t1)
