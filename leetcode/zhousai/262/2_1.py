"""
optimal
"""


class Solution:
    def minOperations(self, grid, x: int) -> int:

        m = len(grid)
        n = len(grid[0])

        targetls = [x for y in grid for x in y]

        targetls.sort()

        tlen = len(targetls)

        median = targetls[tlen // 2] if tlen % 2 == 1 else targetls[tlen // 2 - 1]

        ans = 0
        for i in range(m):
            for j in range(n):
                if abs(grid[i][j] - median) % x != 0:
                    return -1
                ans += abs(grid[i][j] - median) // x

        return ans
