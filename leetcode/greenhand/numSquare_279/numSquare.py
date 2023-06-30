"""
author:wjw
分析：dp[i]表示和为i的最少数量。
"""
import math


class Solution:
    def numSquare(self, n):

        x = float('inf')
        dp = [x] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            max_num = math.floor(math.sqrt(i))
            for j in range(1, max_num + 1):
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)

        return dp[n]


n = 8441
res = Solution().numSquare(n)
print(res)
