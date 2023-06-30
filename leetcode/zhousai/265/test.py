import heapq


class Solution:
    def trapRainWater(self, heightMap) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        visited = [[False for i in range(n)] for i in range(m)]

        heap = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        ans = 0
        while heap:
            height, x, y = heapq.heappop(heap)

            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False:
                    if height > heightMap[nx][ny]:
                        ans += height - heightMap[nx][ny]
                        print(height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        return ans

heightMap=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
res=Solution().trapRainWater(heightMap)
print(res)