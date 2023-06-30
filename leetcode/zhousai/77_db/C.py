class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls) -> int:

        grid = [[0] * n for _ in range(m)]  # 初始态为0,g为1，w为2，看得到为3
        for x,y in guards:
            grid[x][y]=1

        for x,y in walls:
            grid[x][y]=2

        d=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:

                    for dx,dy in d:
                        x=i+dx
                        y=j+dy
                        while 0<=x<m and 0<=y<n and (grid[x][y]==0 or grid[x][y]==3):
                            grid[x][y]=3
                            x+=dx
                            y+=dy


        return sum(grid[i][j]==0 for i in range(m) for j in range(n))


m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
m = 3
n = 3
guards = [[1,1]]
walls = [[0,1],[1,0],[2,1],[1,2]]
res=Solution().countUnguarded(m,n,guards,walls)
print(res)