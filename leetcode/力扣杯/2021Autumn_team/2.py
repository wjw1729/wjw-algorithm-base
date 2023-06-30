from collections import deque
class Solution:
    def bicycleYard(self, position, terrain, obstacle) :

        m = len(terrain)
        n = len(terrain[0])

        speed = [[float('inf')] * n for _ in range(m)]
        speed[position[0]][position[1]] = 1

        queue = deque()
        queue.append((position[0], position[1], 1))

        bin = set()
        bin.add((position[0], position[1], 1))

        while queue:
            r, c, v = queue.popleft()

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    tmp = speed[r][c] + terrain[r][c] - terrain[x][y] - obstacle[x][y]
                    if 0 < tmp < speed[x][y]:
                        speed[x][y] = tmp
                    if tmp > 0 and (x, y, tmp) not in bin:
                        queue.append((x, y, tmp))
                        bin.add((x, y, tmp))

        ans = []
        for i in range(m):
            for j in range(n):
                if speed[i][j] == 1 and [i, j] != position:
                    ans.append([i, j])

        ans.sort(key=lambda x: (x[0], x[1]))

        return ans

position = [1,1]
terrain = [[5,0],[0,6]]
obstacle = [[0,6],[7,0]]
res=Solution().bicycleYard(position,terrain,obstacle)
print(res)