from collections import  deque,defaultdict
class Solution:
    def countPaths(self, grid) -> int:

        mod=10**9+7
        m=len(grid)
        n=len(grid[0])

        f=[[0]*n for _ in range(m)]


        vmap=defaultdict(list)
        for i in range(m):
            for j in range(n):
                vmap[grid[i][j]].append((i,j))


        for k,v in sorted(vmap.items(),key=lambda x:x[0]):
            for x,y in v:
                f[x][y]=1
                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0<=nx<m and 0<=ny<n:
                        f[x][y]+=f[nx][ny]
                        f[x][y]%=mod



        return sum(sum(x)%mod for x in f)%mod


