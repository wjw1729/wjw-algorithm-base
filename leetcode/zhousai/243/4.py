"""
author:wjw
分析：动态规划
时间复杂度:O(n**2)
"""


class Solution:
    def mnSkips(self, dist, speed, hoursBefore):

        n = len(dist)
        f = [[float('inf')] * n for _ in range(n + 1)]

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(n):
                f[i][j] = min(
                    (f[i - 1][j] + (dist[i - 1] - 1) / speed) // 1 + 1 if f[i - 1][j] != float('inf') else float('inf'),
                    (f[i - 1][j - 1] if j > 0 else float('inf')) + dist[
                        i - 1] / speed)  ####向上取整可以转换为向下取整来求。math.ceil(a/b)=(a-1)//b+1

        for j in range(n):
            if f[n][j] <= hoursBefore:
                return j

        return -1


dist = [1, 3, 2]
speed = 4
hoursBefore = 2
dist = [7, 3, 5, 5]
speed = 2
hoursBefore = 10
res = Solution().mnSkips(dist, speed, hoursBefore)
print(res)
