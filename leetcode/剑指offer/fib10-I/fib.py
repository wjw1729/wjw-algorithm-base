"""
author:wjw
分析：Olog(n)实现fib求法。
"""


def onfib(n):
    fn_2 = 0
    fn_1 = 1
    if n == 0:
        return fn_2
    if n == 1:
        return fn_1
    for i in range(2, n + 1):
        now = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = now

    return now


class Solution:
    def fib(self, n):

        def matmulti(x1, x2):
            x = [[0, 0], [0, 0]]
            x[0][0] = x1[0][0] * x2[0][0] + x1[0][1] * x2[1][0]
            x[0][1] = x1[0][0] * x2[0][1] + x1[0][1] * x2[1][1]
            x[1][0] = x1[1][0] * x2[0][0] + x1[1][1] * x2[1][0]
            x[1][1] = x1[1][0] * x2[0][1] + x1[1][1] * x2[1][1]
            return x

        if n == 0:
            return 0
        if n == 1:
            return 1
        M = [[1, 1], [1, 0]]
        N = [[1], [0]]

        def compute(M, k):
            if k == 1:
                return M
            if k % 2 == 0:
                res = compute(M, k // 2)
                return matmulti(res, res)
            else:
                res = compute(M, k // 2)
                return matmulti(matmulti(res, res), M)

        ans = compute(M, n - 1)
        return ans[0][0]


n = 45
res1 = Solution().fib(n)
res2 = onfib(n)
print(res1)
print(res2)
