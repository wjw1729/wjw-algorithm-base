"""
author:wjw
分析：
优化：可以用np优化计算
"""
import numpy as np

class Solution:
    def countPoints(self, points, queries):
        points_num = len(points)
        circle_num = len(queries)

        ans = [0] * circle_num

        for i in range(circle_num):
            num = 0
            for j in range(points_num):
                x, y = points[j][0], points[j][1]
                x0, y0, r0 = queries[i][0], queries[i][1], queries[i][2]
                if r0 ** 2 >= (x - x0) ** 2 + (y - y0) ** 2:
                    num += 1

            ans[i] = num

        return ans


points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
res = Solution().countPoints(points, queries)
print(res)
