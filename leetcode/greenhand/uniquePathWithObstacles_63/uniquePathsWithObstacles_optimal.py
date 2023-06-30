"""
author:wjw
分析：动态规划+优化
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if 1 in obstacleGrid[0]:
            index = obstacleGrid[0].index(1)
            dp = [1] * index + [0] * (n - index)
        else:
            dp = [1] * n

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if j == 0:
                        continue
                    dp[j] = dp[j - 1] + dp[j]
                else:
                    dp[j] = 0
        return dp[-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 1], [0, 0]]

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

res = Solution().uniquePathsWithObstacles(obstacleGrid)
print(res)
