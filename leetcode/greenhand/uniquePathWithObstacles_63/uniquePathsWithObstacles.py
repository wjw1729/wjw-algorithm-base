"""
author:wjw
分析：动态规划
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        dp[0][0] = 1
                        continue
                    if i == 0:
                        dp[i][j] = dp[i][j - 1]
                        continue
                    if j == 0:
                        dp[i][j] = dp[i - 1][j]
                        continue
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 1], [0, 0]]

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 0], [1, 1], [0, 0]]
res = Solution().uniquePathsWithObstacles(obstacleGrid)
print(res)
