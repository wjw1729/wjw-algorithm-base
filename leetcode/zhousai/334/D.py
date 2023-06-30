from collections import deque
import heapq
import time


class Solution:
    def minimumTime(self, grid):
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m = len(grid)
        n = len(grid[0])

        tls = [[float('inf')] * n for _ in range(m)]

        tls[0][0] = 0

        q = []
        heapq.heappush(q,(0,0,0))


        def get(i, j, t):
            if grid[i][j] <= t + 1:
                return t + 1
            if (grid[i][j] - (t + 1)) % 2 == 0:
                return grid[i][j]
            return grid[i][j] + 1

        while q:
            t,x, y = heapq.heappop(q)
            if x==m-1 and y==n-1:
                return t

            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n:

                    tmp = get(nx, ny, t)
                    if tmp < tls[nx][ny]:
                        tls[nx][ny] = tmp
                        heapq.heappush(q,( tmp,nx, ny))

        return tls[-1][-1]

grid=[[0,100,1,1,1],[1,100,9,100,1],[1,1,1,100,1],[100,100,100,100,1],[100,100,100,100,1]]
res=Solution().minimumTime(grid)
print(res)

