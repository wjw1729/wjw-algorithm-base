class Solution:
    def minPathCost(self, grid, moveCost) -> int:

        m=len(grid)
        n=len(grid[0])
        f=[[float('inf')]*n for _ in range(m)]

        f[0]=[grid[0][j] for j in range(n)]


        for i in range(m-1):
            for j in range(n):

                for k in range(n):
                    f[i+1][k]=min(f[i+1][k],f[i][j]+moveCost[grid[i][j]][k]+grid[i+1][k])




        return min(f[m-1])
