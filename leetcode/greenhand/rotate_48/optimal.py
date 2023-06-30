"""
author:wjw
分析：转置（手动）+reverse。牛的
"""


class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(n):
            matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)
