"""
author:wjw
分析：回溯算法
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ans = []
        def backtrack(x, y):

            if x == m - 1 and y == n - 1:
                ans.append(1)
                return

            if x < m - 1:
                backtrack(x + 1, y)

            if y < n - 1:
                backtrack(x, y + 1)

        backtrack(0, 0)
        return len(ans)


m = 3
n = 3
res = Solution().uniquePaths(m, n)
print(res)
