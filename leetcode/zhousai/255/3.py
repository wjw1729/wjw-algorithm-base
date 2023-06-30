class Solution:
    def minimizeTheDifference(self, mat, target: int) -> int:

        m, n = len(mat), len(mat[0])

        f = {0}
        minlarge=float('inf')
        for i in range(m):
            g = set()
            levellarge=float('inf')
            for x in mat[i]:
                for y in f:
                    if x+y>target:
                        levellarge=min(levellarge,x+y)
                    else:
                        g.add(x + y)

                levellarge=min(levellarge,minlarge+x)
            f = g
            minlarge=levellarge

        ans = minlarge-target
        for x in f:
            ans = min(ans, abs(x - target))

        return ans


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 13
res = Solution().minimizeTheDifference(mat, target)
print(res)
