"""
author:wjw
分析：动态规划.dp[k][i][j]表示在i，j处恰好移动k步能够出界的方案数。
    时间复杂度：O(mn*maxMove)
    可以优化为二维的。
"""


class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        if m == n == 1:
            return 4
        dp = [[[0] * n for i in range(m)] for _ in range(maxMove + 1)]

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if k == 1:
                        if m > 1 and n > 1:
                            if (i == 0 and j == 0) or (i == 0 and j == n - 1) or (i == m - 1 and j == 0) or (
                                    i == m - 1 and j == n - 1):
                                dp[k][i][j] = 2
                            elif i == 0 or i == m - 1 or j == 0 or j == n - 1:
                                dp[k][i][j] = 1
                            else:
                                dp[k][i][j] = 0
                        else:
                            if m == 1:
                                if j == 0 or j == n - 1:
                                    dp[k][i][j] = 3
                                else:
                                    dp[k][i][j] = 2
                            if n == 1:
                                if i == 0 or i == m - 1:
                                    dp[k][i][j] = 3
                                else:
                                    dp[k][i][j] = 2

                    else:
                        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                            if 0 <= x < m and 0 <= y < n:
                                dp[k][i][j] = (dp[k][i][j] + dp[k - 1][x][y]) % (10 ** 9 + 7)

        return sum([dp[x][startRow][startColumn] for x in range(maxMove + 1)])


m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
res = Solution().findPaths(m, n, maxMove, startRow, startColumn)
print(res)
