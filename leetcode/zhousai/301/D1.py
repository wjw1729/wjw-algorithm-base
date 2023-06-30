class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        f = [[[0] * n for _ in range(n)] for _ in range(2 * n - 1)]

        for i in range(2 * n - 1):
            for j in range(n):
                for k in range(n):

                    if i<j or i<k or i - j >= n  or i - k >= n or grid[j][i - j] == -1 or grid[k][i - k] == -1:
                        f[i][j][k] = -float('inf')
                        continue

                    a = f[i - 1][j][k] + (grid[j][i - j] + grid[k][i - k] if j != k else grid[j][i - j])
                    b = (f[i - 1][j - 1][k] + (grid[j][i - j] + grid[k][i - k] if j != k else grid[j][i - j])) if j-1>=0 else -float('inf')
                    c = (f[i - 1][j][k - 1] + (grid[j][i - j] + grid[k][i - k] if j != k else grid[j][i - j])) if k-1>=0 else -float('inf')
                    d = (f[i - 1][j - 1][k - 1] + (grid[j][i - j] + grid[k][i - k] if j != k else grid[j][i - j])) if (j-1>=0 and k-1>=0) else -float('inf')

                    f[i][j][k] = max(a, b, c, d)

        return f[2 * n - 2][n - 1][n - 1]

grid =[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
res=Solution().cherryPickup(grid)
print(res)