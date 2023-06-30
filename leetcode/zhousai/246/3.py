"""
author：wjw
分析：岛屿
"""


import collections
class Solution:
    def countSubIslands(self,grid1,grid2):
        m=len(grid1)
        n=len(grid1[0])

        ans=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    check=True
                    neighbor=collections.deque()
                    neighbor.append((i,j))
                    grid2[i][j]=0
                    if grid1[i][j]==0:
                        check=False

                    while neighbor:
                        r,c=neighbor.popleft()
                        for x,y in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                            if 0<=x<m and 0<=y<n and grid2[x][y]==1:
                                neighbor.append((x,y))
                                grid2[x][y]=0
                                if grid1[x][y]==0:
                                    check=False

                    if check:
                        ans+=1

        return ans


grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
res=Solution().countSubIslands(grid1,grid2)
print(res)