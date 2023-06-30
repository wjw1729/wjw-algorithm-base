class Solution:
    def possibleToStamp(self, grid, stampHeight: int, stampWidth: int) -> bool:

        m = len(grid)
        n = len(grid[0])

        if sum(sum(x) for x in grid) == m * n:
            return True

        if m < stampHeight or n < stampWidth:
            return False

        hdls = [[] for _ in range(n)]
        wdls = [[] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hdls[j].append(i)
                    wdls[i].append(j)

        mindh = m
        for i in range(n):
            pre = -1
            for x in hdls[i]:
                if x-pre-1>0:
                    mindh = min(mindh, x - pre - 1)
                    if mindh < stampHeight:
                        return False
                pre = x

            if m-pre-1>0:
                mindh = min(mindh, m - pre - 1)
                if mindh < stampHeight:
                    return False

        mindw = n
        for i in range(m):
            pre = -1
            for y in wdls[i]:
                if y-pre-1>0:
                    mindw = min(mindw, y - pre - 1)
                    if mindw < stampWidth:
                        return False
                pre = y

            if n-pre-1>0:
                mindw = min(mindw, n - pre - 1)
                if mindw < stampWidth:
                    return False

        return True

grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
stampHeight=4
stampWidth=3
res=Solution().possibleToStamp(grid,stampHeight,stampWidth)
print(res)