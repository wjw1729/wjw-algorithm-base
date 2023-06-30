"""
author:off
分析：dp[i][j][k]
"""


class Solution:
    def checkRecord(self, n):
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]

        dp[0][0][0] = 1
        dp[0][1][0] = 1
        dp[0][0][1] = 1

        for i in range(1, n):
            dp[i][0][0] = sum(dp[i - 1][0][x] for x in range(3))

            dp[i][1][0] = sum(dp[i - 1][0][x] for x in range(3))+sum(dp[i-1][1][x] for x in range(3))

            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][1][1] = dp[i - 1][1][0]

            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][2] = dp[i - 1][1][1]

        ans = 0
        for j in range(2):
            for k in range(3):
                ans += dp[n - 1][j][k]

        return ans % (10 ** 9 + 7)


n = 10101
res = Solution().checkRecord(n)
print(res)
