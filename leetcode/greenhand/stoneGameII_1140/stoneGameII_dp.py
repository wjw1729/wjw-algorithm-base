"""
authro:wjw
分析：动态规划。dp[i][j]表示剩下piles[i:]的情况下，M=j的挑选者（是会随着递推的进行而变化的）能选的最大石头数量。
"""


class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]

        suffixsum = 0
        for i in range(n - 1, -1, -1):
            suffixsum += piles[i]
            for M in range(1, n):
                if i + 2 * M >= n:
                    dp[i][M] = suffixsum
                else:
                    for x in range(1, 2 * M + 1):
                        dp[i][M] = max(dp[i][M], suffixsum - dp[i + x][max(M, x)])

        return dp[0][1]


piles = [2, 7, 9, 4, 4]
piles = [3111, 4303, 2722, 2183, 6351, 5227, 8964, 7167, 9286, 6626, 2347, 1465, 5201, 7240, 5463, 8523, 8163, 9391,
         8616, 5063, 7837, 7050, 1246, 9579, 7744, 6932, 7704, 9841, 6163, 4829, 7324, 6006, 4689, 8781, 621]
res = Solution().stoneGameII(piles)
print(res)
