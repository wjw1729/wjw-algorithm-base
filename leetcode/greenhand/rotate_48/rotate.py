"""
author:wjw
分析：用另一个矩阵实现。顺时针旋转=转置+轴对称
"""


class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)

        ans = [[[0] for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                ans[j][i] = matrix[i][j]

        for i in range(n):
            ans[i].reverse()

        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Solution().rotate(matrix)
print(res)
