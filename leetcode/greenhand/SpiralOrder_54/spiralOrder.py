"""
author:wjw
分析：
"""


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        ans = [matrix[0][0]]

        right = n
        bottom = m
        left = -1
        up = 0

        while len(ans) < m * n:

            while j < right:
                j += 1
                if j < right:
                    ans.append(matrix[i][j])

            j -= 1
            right -= 1

            if len(ans) == m * n:
                break
            while i < bottom:
                i += 1
                if i < bottom:
                    ans.append(matrix[i][j])
            i -= 1
            bottom -= 1

            if len(ans) == m * n:
                break

            while j > left:
                j -= 1
                if j > left:
                    ans.append(matrix[i][j])

            j += 1
            left += 1

            if len(ans) == m * n:
                break

            while i > up:
                i -= 1
                if i > up:
                    ans.append(matrix[i][j])

            i += 1
            up += 1

        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
res = Solution().spiralOrder(matrix)
print(res)
