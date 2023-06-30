"""
author:wjw
分析：dp[i][j][k]表示到第i位以{0:'P',1:’L‘，2：’LL‘,3:'A'}结尾，是否出现过’A‘（k=0,表示未出现过，k=1表示出现过）的总数。
这也会超时啊！牛的。
"""

import time


class Solution:
    def checkRecord(self, n):
        dp = [[[0] * 2 for _ in range(4)] for _ in range(n)]

        dp[0][0][0] = 1
        dp[0][1][0] = 1
        dp[0][3][1] = 1
        for i in range(1, n):
            dp[i][0][0] = sum(dp[i - 1][x][0] for x in range(4))
            dp[i][0][1] = sum(dp[i - 1][x][1] for x in range(4))

            dp[i][1][0] = dp[i - 1][0][0]
            dp[i][1][1] = dp[i - 1][0][1] + dp[i - 1][3][1]

            dp[i][2][0] = dp[i - 1][1][0]
            dp[i][2][1] = dp[i - 1][1][1]

            dp[i][3][1] = sum(dp[i - 1][x][0] for x in range(4))

        return sum(dp[n - 1][x][0] + dp[n - 1][x][1] for x in range(4)) % (10 ** 9 + 7)


t1 = time.time()
n = 10101
res = Solution().checkRecord(n)
print(res)
print(time.time() - t1)
