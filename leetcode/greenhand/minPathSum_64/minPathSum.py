"""
author:wjw
分析:动态规划
"""


class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == [0]:
                    dp[0][0] = grid[0][0]
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[0][j]
                    continue
                if j == 0:
                    dp[i][0] = dp[i - 1][0] + grid[i][0]
                    continue
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[m - 1][n - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid = [[1, 2, 3], [4, 5, 6]]
res = Solution().minPathSum(grid)
print(res)
