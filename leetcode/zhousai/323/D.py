from collections import deque


class Solution:
    def maxPoints(self, grid, queries):
        m = len(grid)
        n = len(grid[0])
        k = len(queries)
        res = [0] * k

        qls = list(enumerate(queries))
        qls.sort(key=lambda x: x[1])

        q = deque([(0, 0)])
        vis = set()
        vis.add((0, 0))
        ans = 1

        for idx, qnum in qls:

            qqls = deque()
            if qnum <= grid[0][0]:
                continue
            if ans == m * n:
                res[idx] = ans
                continue
            # print(q)
            while q:
                x, y = q.popleft()

                bao = False
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] < qnum:
                            if (nx, ny) not in vis:
                                q.append((nx, ny))
                                vis.add((nx, ny))
                                ans += 1
                        else:
                            bao = True
                if bao:
                    qqls.append((x, y))

            q = qqls
            res[idx] = ans

        return res


grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
grid = [[5, 2, 1], [1, 1, 2]]
queries = [3]
res = Solution().maxPoints(grid, queries)
print(res)
