"""
author:wjw
分析：动态规划优化。
    转换为状态转移方程矩阵形式+快速幂。
    时间复杂度：O（logn）
"""


class Solution:
    def checkRecord(self, n):
        if n == 1:
            return 3

        M = [[0] * 8 for _ in range(8)]
        M[0] = [1, 0] * 4
        M[1] = [0, 1] * 4
        M[2][0] = 1
        M[3][1] = 1
        M[3][-1] = 1
        M[4][2] = 1
        M[5][3] = 1
        M[7] = [1, 0] * 4

        N = [1, 0, 1, 0, 0, 0, 0, 1]

        def matmultiply(x, y):
            z = [[0] * 8 for _ in range(8)]

            for i in range(8):
                for j in range(8):
                    for k in range(8):
                        z[i][j] += x[i][k] * y[k][j]

            return z

        def compute(M, n):
            if n == 1:
                return M

            if n % 2 == 0:
                res = compute(M, n // 2)
                return matmultiply(res, res)
            else:
                res = compute(M, n // 2)
                return matmultiply(matmultiply(res, res), M)

        M_k = compute(M, n - 1)
        ans = 0
        for i in range(8):
            for j in range(8):
                if j == 0 or j == 2 or j == 7:
                    ans += M_k[i][j]

        return ans % (10 ** 9 + 7)


n = 10101
res = Solution().checkRecord(n)
print(res)
