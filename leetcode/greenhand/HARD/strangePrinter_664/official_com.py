"""
author:wjw
分析：dp[i][j]表示[str(i)~str(j)]时的最少打印次数.注意动态规划开始的方向。
"""


class Solution:
    def strangePrinter(self, s) -> int:
        n = len(s)
        x = float('inf')
        dp = [[x for i in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]

                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][n - 1]


str = 'abab'
res = Solution().strangePrinter(str)
print(res)
