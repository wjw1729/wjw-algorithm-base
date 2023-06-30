"""
author:wjw
分析：
"""
import itertools


class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 1

        row_sum = [[0] * (n + 1) for i in range(m)]

        for i in range(m):
            row_sum[i] = [0] + list(itertools.accumulate(grid[i]))

        col_sum = [[0] for i in range(n)]

        for i in range(n):
            total = 0
            for j in range(m):
                total += grid[j][i]
                col_sum[i].append(total)

        for i in range(m):
            for j in range(n):

                k_range = min(m - i, n - j)
                if i == 1 and j == 1:
                    print('k_range', k_range)
                for k in range(2, k_range + 1):  # k表示长度
                    not_magic = False
                    print(k)

                    if k == 3:
                        print(k)

                    a = row_sum[i][j + k] - row_sum[i][j]

                    for l in range(i + 1, i + k):
                        if row_sum[l][j + k] - row_sum[l][j] != a:
                            not_magic = True
                            break
                    if not_magic == True:
                        continue
                    for l in range(j, j + k):
                        if col_sum[l][i + k] - col_sum[l][i] != a:
                            not_magic = True
                            break
                    if not_magic == True:
                        continue
                    x = 0
                    for l in range(0, k):
                        x += grid[i + l][j + l]
                    if x != a:
                        break

                    x = 0
                    for l in range(0, k):
                        x += grid[i + l][j + k - 1 - l]
                    if x != a:
                        break
                    ans = max(ans, k)
        return ans


grid = [[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]
grid = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
res = Solution().largestMagicSquare(grid)
print(res)
