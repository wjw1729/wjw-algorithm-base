class Solution:
    def generateMatrix(self, n: int):

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ans = [[0] * n for _ in range(n)]
        ans[0][0] = 10
        i, j = 0, 0
        k = 0
        right = n - 1
        left = 0
        up = 1
        down = n - 1
        for total in range(n ** 2 - 1):
            delta_x, delta_y = direction[k]

            i += delta_x
            j += delta_y
            ans[i][j] = total + 2

            if k == 0 and j == right:
                right -= 1
                k = 1

            if k == 1 and i == down:
                down -= 1
                k = 2
            if k == 2 and j == left:
                left += 1
                k = 3
            if k == 3 and i == up:
                up += 1
                k = 0

        return ans


n = 3
res = Solution().generateMatrix(n)
print(res)
