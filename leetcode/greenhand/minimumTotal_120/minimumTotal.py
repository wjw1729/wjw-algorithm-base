"""
author:wjw
分析：动态规划，空间复杂度:O(n^2).
优化：为了减少空间复杂度，可以设置两个列表为dp_last(1*n),dp_now(1*n)表示上一层和这层的最短路径。空间复杂度为O(n)
"""


class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = triangle.copy()

        for i in range(n):
            for j in range(len(dp[i])):
                if i == 0 and j == 0:
                    dp[0][0] = triangle[0][0]
                    continue
                if j == 0:
                    dp[i][0] = dp[i - 1][j] + triangle[i][j]
                    continue
                if j == len(dp[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                    continue
                dp[i][j] = min(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])

        return min(dp[n - 1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res = Solution().minimumTotal(triangle)
print(res)
