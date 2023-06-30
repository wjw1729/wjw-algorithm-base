from collections import deque
class Solution:
    def cutOffTree(self, forest) -> int:

        n = len(forest)
        m = len(forest[0])

        pls = []
        for i in range(n):
            for j in range(m):
                if (i==0 and j==0) or forest[i][j]>1:
                    pls.append((i, j, forest[i][j]))

        pls.sort(key=lambda x: x[2])
        pls=[(0,0)]+pls


        ans = 0
        for i in range(len(pls) - 1):
            s = pls[i]
            t = pls[i + 1]

            queue = deque()
            queue.append((s[0], s[1], 0))

            check = False
            vis=set()
            vis.add((s[0],s[1]))
            while queue:
                x, y, l = queue.popleft()
                if (x, y) == (t[0], t[1]):
                    check = True
                    ans += l
                    break
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in vis:
                        if forest[nx][ny] != 0:
                            queue.append((nx, ny, l + 1))
                            vis.add((nx,ny))

            if not check:
                return -1

        return ans



forest = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
res=Solution().cutOffTree(forest)
print(res)