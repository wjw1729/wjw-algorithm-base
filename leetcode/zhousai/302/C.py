from collections import deque


class Solution:
    def containVirus(self, isInfected) -> int:

        m = len(isInfected)
        n = len(isInfected[0])

        ans = 0

        while 1:

            neghbors = []
            fw = []

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:

                        idx = len(neghbors) + 1
                        nb = set()
                        walls = 0
                        q = deque()
                        q.append((i, j))
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()

                            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        nb.add((nx, ny))
                                        walls += 1

                        neghbors.append(list(nb))
                        fw.append(walls)

            if not neghbors:
                break

            nbmax = 0
            for i in range(len(fw)):
                if len(neghbors[i]) > nbmax:
                    idx = i
                    nbmax = len(neghbors[i])

            ans += fw[idx]

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == -idx - 1:
                        isInfected[i][j] = 2
                    elif isInfected[i][j] < 0:
                        isInfected[i][j] = 1

            for i in range(len(fw)):
                if i == idx:
                    continue
                for x, y in neghbors[i]:
                    isInfected[x][y] = 1

            if len(neghbors) == 1:
                break

        return ans


isInfected = [[0, 0, 1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [1, 1, 0, 0, 0, 1, 0, 1, 0, 0]]

res = Solution().containVirus(isInfected)
print(res)
