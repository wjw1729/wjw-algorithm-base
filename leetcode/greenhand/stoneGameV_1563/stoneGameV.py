"""
author:wjw
分析：动态规划origin.dp[l][r]表示该轮Alice能够从l-r这堆中获得的最大的得分。
"""


class Solution:
    def stoneGameV(self, stoneValue):

        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:
                    continue
                for i in range(l + 1, r + 1):
                    if sum(stoneValue[l:i]) > sum(stoneValue[i:r + 1]):
                        dp[l][r] = max(dp[l][r], sum(stoneValue[i:r + 1]) + dp[i][r])
                    elif sum(stoneValue[l:i]) < sum(stoneValue[i:r + 1]):
                        dp[l][r] = max(dp[l][r], sum(stoneValue[l:i]) + dp[l][i - 1])
                    else:
                        res = max(dp[l][i - 1], dp[i][r]) + sum(stoneValue[l:i])
                        dp[l][r] = max(dp[l][r], res)

        return dp[0][n - 1]


stoneValue = [6, 2, 3, 4, 5, 5]
stoneValue = [7, 7, 7, 7, 7, 7, 7]
stoneValue = [4]
res = Solution().stoneGameV(stoneValue)
print(res)
