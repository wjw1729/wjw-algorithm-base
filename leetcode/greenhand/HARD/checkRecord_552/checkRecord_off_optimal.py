"""
author:wjw
分析：每个时刻进行6个状态的划分即可。
快速幂。O(logn)
"""


class Solution:
    def checkRecord(self, n):
        MOD=10**9+7
        if n == 1:
            return 3
        M = [[0] * 6 for _ in range(6)]
        M[0] = [1, 0] * 3
        M[1] = [1] * 6
        M[2][0] = 1
        M[3][1] = 1
        M[4][2] = 1
        M[5][3] = 1

        N = [[1], [1], [1], [0], [0], [0]]
        N = [[1]] * 3 + [[0]] * 3

        def matmultiply(x, y):
            m = len(x)
            n = len(x[0])
            q = len(y[0])

            z = [[0] * q for _ in range(m)]

            for i in range(m):
                for k in range(q):
                    for j in range(n):
                        z[i][k] += x[i][j] * y[j][k]
                        z[i][k]%=MOD

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

        ans = matmultiply(compute(M, n - 1), N)

        return sum([x[0] for x in ans]) % (10 ** 9 + 7)


n = 10101
res = Solution().checkRecord(n)
print(res)
