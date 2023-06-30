"""
author:wjw
分析：dp[i][j]表示当剩下i到j时，最小差值（为负）。当前玩家不一定是先手玩家。
    与预测玩家486的区别是，前者目标是尽可能选大的，该题目标是尽可能选小的。
"""


class Solution:
    def stonesGameVII(self, stones):
        totalsum = sum(stones)
        n = len(stones)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = stones[i]
                else:
                    dp[i][j] = min(stones[i] - dp[i + 1][j], stones[j] - dp[i][j - 1])

        return (totalsum - dp[0][n - 1]) // 2


stones = [5, 3, 1, 4, 2]
stones = [7, 90, 5, 1, 100, 10, 10, 2]
res = Solution().stonesGameVII(stones)
print(res)
