"""
author:wjw
分析：dp[i]表示到i的着色总数
    dp_equal[i]
    dp_notequal[i]
"""


class Solution:
    def colorTheGrid(self, m, n):

        dp = [0] * (m * n)
        dp[0] = 3
        dp_equal = [0] * (m * n)
        dp_notequal = [0] * (m * n)

        for i in range(1, m * n):
            if i < n:
                dp[i] = dp[i - 1] * 2
                continue

            if i % n == 0:
                dp[i] = dp[i - 1] * 2
                dp_equal[i] = dp[i - 1]
                dp_notequal[i] = dp[i] - dp_equal[i]
                continue

            dp[i] = dp_notequal[i - 1] + dp_equal[i - 1] * 2

            dp_equal[i] = dp[i -1]-(2*dp[i-2])
            dp_notequal[i] = dp[i] - dp_equal[i]

        return dp[-1] % (10 ** 9 + 7)


m = 5
n = 5
res = Solution().colorTheGrid(m, n)
print(res)
