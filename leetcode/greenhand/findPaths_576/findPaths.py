"""
author:wjw
分析：广度优先搜索，会超时！
"""

class Solution:
    def findPaths(self,m,n,maxMove,startRow,startColumn):
        ans = 0

        queue = [(startRow, startColumn, 0)]

        while queue:
            r, c, move = queue.pop(0)

            if move == maxMove:
                continue

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if x == -1 or x == m or y == -1 or y == n:
                    ans = (ans + 1) % (10 ** 9 + 7)
                    continue
                if 0 <= x < m and 0 <= y < n:
                    queue.append((x, y, move + 1))

        return ans
