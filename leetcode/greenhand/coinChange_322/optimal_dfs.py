"""
author:wjw
分析：dfs好像可以快很多？
    不知道有什么问题？慢慢慢
"""

import math
import time

class Solution:
    def coinChange(self, coins, amount):

        n = len(coins)
        coins.sort(reverse=True)
        self.mincoins = float('inf')

        def dfs(index, target, total):
            coin = coins[index]
            if math.ceil(target / coin) + total >= self.mincoins:
                return

            if target % coin == 0:
                self.mincoins = total + target // coin
                return

            if index == n - 1:
                return

            for j in range(target // coin, -1, -1):
                dfs(index + 1, target - coin * j, total + j)

        dfs(0, amount, 0)

        return self.mincoins if self.mincoins != float('inf') else -1


t1=time.time()
coins = [1, 2, 5]
coins=[411,412,413,414,415,416,417,418,419,420,421,422]
amount = 9864
res = Solution().coinChange(coins, amount)
print(res)
print(time.time()-t1)