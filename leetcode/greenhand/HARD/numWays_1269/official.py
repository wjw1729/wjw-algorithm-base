"""
author:wjw
分析：dp[i][j]表示i步操作后位于j的方案数.注意方程不能转移时的边界条件。求数目的题基本都可以使用dp来做。
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        j_range = min(arrLen - 1, steps)
        dp = [[[0] for i in range(j_range + 1)] for j in range(steps + 1)]

        for i in range(steps + 1):
            for j in range(j_range + 1):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                    continue
                if i == 0 and j != 0:
                    dp[i][j] = 0
                    continue

                if j == 0:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1])%(10**9+7)
                    continue

                if j == j_range:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1])%(10**9+7)
                    continue

                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1] + dp[i - 1][j]) % (10 ** 9 + 7)

        return dp[steps][0]


steps = 15
arrLen = 15
res = Solution().numWays(steps, arrLen)
print(res)
