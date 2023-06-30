"""
author:wjw
分析：Dijkstra算法。
    时间复杂度:O(mnlogmn)
"""

import heapq
class Solution:
    def minimumEffortPath(self,heights):
        m,n=len(heights),len(heights[0])
        heap=[(0,0,0)]
        dist=[0]+[float('inf')]*(m*n-1)
        seen=set()

        while heap:
            d,x,y=heapq.heappop(heap)

            if (x,y) in seen:
                continue
            if (x,y)==(m-1,n-1):
                break

            seen.add((x,y))

            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=nx<m and 0<=ny<n and max(d,abs(heights[x][y]-heights[nx][ny]))<dist[nx*n+ny]:
                    dist[nx*n+ny]=max(d,abs(heights[x][y]-heights[nx][ny]))
                    heapq.heappush(heap,(dist[nx*n+ny],nx,ny))

        return dist[m*n-1]

heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
#heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]

#heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]

res = Solution().minimumEffortPath(heights)
print(res)
