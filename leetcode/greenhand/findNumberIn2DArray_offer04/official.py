"""
author:wjw
分析：从右上角到左下角，遇到小的就往下，遇到大的就往左。Attention：注意下标越界的问题。
"""


class Solution:
    def findNumberIn2DArray(self, matrix, target):

        if matrix == [] or matrix == [[]]:
            return False
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m - 1

        if matrix[i][j] == target:
            return True

        while (i, j) != (n - 1, 0):
            if (matrix[i][j] > target or i == n - 1) and j != 0:
                j = j - 1
            elif (matrix[i][j] < target or j == 0) and i != n - 1:
                i = i + 1

            if matrix[i][j] == target:
                return True

        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
matrix = [[1, 1]]
# matrix=[[-1],[-1]]

target = 5
res = Solution().findNumberIn2DArray(matrix, target)
print(res)
