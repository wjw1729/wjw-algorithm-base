"""
author:wjw
分析：dp[i][l]表示以i开头的的长度为l的list的数量。
"""


class Solution:
    def maxPlanNumbers(self, n, m):

        MOD = 998244353
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if j == 1:
                    dp[i][j] = 1
                else:
                    for k in range(1, n // i + 1):
                        dp[i][j] += dp[i * k][j - 1]
                        dp[i][j] %= MOD
        ans = 0
        for i in range(1, n + 1):
            ans += dp[i][m]
            ans %= MOD

        return ans


n = 4
m = 3
res = Solution().maxPlanNumbers(n, m)
print(res)
