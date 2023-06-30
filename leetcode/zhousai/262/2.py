class Solution:
    def minOperations(self, grid, x: int) -> int:
        m = len(grid)
        n = len(grid[0])

        def minoperate(grid, target) -> int:
            ans = 0
            candivide=True
            for i in range(m):
                for j in range(n):
                    if candivide and abs(grid[i][j] - target)%x!=0:
                        candivide=False
                    ans += abs(grid[i][j] - target)

            return ans,candivide

        targetset = set(y for x in grid for y in x)
        targetls = list(targetset)
        targetls.sort()


        tlen=len(targetls)

        l = 0
        r = tlen - 1

        ans = float('inf')

        while l <= r:
            mid = (l + r + 1) // 2

            tmpl,dl = minoperate(grid, targetls[mid - 1]) if mid >0 else (float('inf'),False)
            tmpm,dm = minoperate(grid, targetls[mid])
            tmpr,dr = minoperate(grid, targetls[mid + 1]) if mid<tlen-1 else (float('inf'),False)

            if dm:
                ans = min(ans, tmpm // x)
            if dl:
                ans = min(ans, tmpl // x)
            if dr:
                ans = min(ans, tmpr // x)

            if tmpl < tmpm < tmpr:
                r = mid-1
            elif tmpl > tmpm > tmpr:
                l = mid+1
            else:
                break

        return ans if ans!=float('inf') else -1

grid=[[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]]
x=84
res=Solution().minOperations(grid,x)
print(res)

