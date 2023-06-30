"""
author:wjw
分析：二分查找.
"""


class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])

        def search(dis):
            queue = [(0, 0)]
            bin = {(0, 0)}

            while queue:
                r, c = queue.pop(0)

                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and abs(heights[x][y] - heights[r][c]) <= dis and (x, y) not in bin:
                        if x == m - 1 and y == n - 1:
                            return True
                        queue.append((x, y))
                        bin.add((x, y))

            return False

        left = 0
        right = 10 ** 6 - 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if search(mid):
                right = mid-1
                ans = right
            else:
                left = mid + 1

        return ans


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
res = Solution().minimumEffortPath(heights)
print(res)
