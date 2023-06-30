class Solution:
    def getLength(self, grid) -> int:

        di=[(1,0),(0,1),()]

        n=len(grid)
        m=len(grid[1])

        def dfs(x,y,p):
            if x<0 or x>=n or y<0 or y>=m:
                return 0


            if grid[x][y]=='L':
                if p==(1,0):
                    p=(0,1)
                elif p==(0,1):
                    p=(1,0)
                elif p==(-1,0):
                    p=(0,-1)
                else:
                    p=(-1,0)

                x+=p[0]
                y+=p[1]

                return dfs(x,y,p)+1

            elif grid[x][y]=='R':
                if p == (1, 0):
                    p = (0, -1)
                elif p == (0, -1):
                    p = (1,0)
                elif p == (-1, 0):
                    p = (0, 1)
                else:
                    p = (-1, 0)

                x += p[0]
                y += p[1]

                return dfs(x, y, p) + 1

            else:
                x+=p[0]
                y+=p[1]

                return dfs(x,y,p)+1

        return dfs(0,0,(1,0))
