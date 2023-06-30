"""
author:wjw
分析：动态规划+3指针
"""


class Solution:
    def nthUglyNumber(self, n):

        dp = [1] * n
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1

        return dp[-1]


n = 10
res = Solution().nthUglyNumber(n)
print(res)
