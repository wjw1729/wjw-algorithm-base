from collections import deque
from functools import lru_cache
import itertools

class Solution:
    def shortestPathAllKeys(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        kls = []
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    kls.append((i, j))
                if grid[i][j] == '@':
                    sp = [i, j]

        mapd = {grid[x][y]: i for i, (x, y) in enumerate(kls)}

        q=deque()
        q.append((sp[0],sp[1],0,0))

        dis=[[[float('inf')]*2**len(kls) for _ in range(n)]  for _ in range(m)]
        dis[sp[0]][sp[1]][0]=0

        while q:
            x,y,mask,d=q.popleft()
            if mask==(1<<len(kls))-1:
                return d


            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny]=='.' or grid[nx][ny]== '@':
                        if d+1<dis[nx][ny][mask]:
                            q.append((nx,ny,mask,d+1))
                            dis[nx][ny][mask]=d+1

                    elif grid[nx][ny].islower():
                        nmask=mask |(1<<mapd[grid[nx][ny]])
                        if d + 1 < dis[nx][ny][nmask]:
                            q.append((nx,ny,nmask,d+1))
                            dis[nx][ny][nmask]=d+1

                    elif grid[nx][ny].isupper():
                        if mask &(1<<mapd[grid[nx][ny].lower()]):
                            if dis[nx][ny][mask]>d+1:
                                q.append((nx,ny,mask,d+1))
                                dis[nx][ny][mask]=d+1
        return -1


grid=["b","A","a","@","B"]
grid=["@...a",".###A","b.BCc"]
grid=[".#.b.","A.#aB","#d...","@.cC.","D...#"]
res=Solution().shortestPathAllKeys(grid)
print(res)