"""
author:wjw
分析：动态规划
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                    continue
                if i == 0:
                    dp[0][j] = 1
                    continue
                if j == 0:
                    dp[i][0] = 1
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


m = 3
n = 3
res = Solution().uniquePaths(m, n)
print(res)
