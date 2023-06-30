"""
author:wjw

优化：为了减少空间复杂度，可以设置两个列表为dp_last(1*n),dp_now(1*n)表示上一层和这层的最短路径。空间复杂度为O(n)
"""


class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp_last = [0] * n
        dp_now = [0] * n

        for i in range(n):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp_now[j] = dp_last[j] + triangle[i][j]
                    continue
                if j == len(triangle[i]) - 1:
                    dp_now[j] = dp_last[j - 1] + triangle[i][j]
                    continue
                dp_now[j] = min(dp_last[j] + triangle[i][j], dp_last[j - 1] + triangle[i][j])

            dp_last = dp_now.copy()
        return min(dp_now)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res = Solution().minimumTotal(triangle)
print(res)
