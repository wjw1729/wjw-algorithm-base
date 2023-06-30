"""
author:wjw
分析：动态规划。提前用动态规划建好回文关系判断的值存储。
"""


class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [float('inf')] * n
        dp[0] = 0
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        for i in range(1, n):
            if g[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if g[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


s = "aab"
res = Solution().minCut(s)
print(res)
