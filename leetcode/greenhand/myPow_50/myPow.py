"""
author:wjw
分析：分治实现log(n)的时间复杂度。
"""


class Solution:
    def myPow(self, x, n):

        def mypositivepow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 1:
                res1 = mypositivepow(x, n // 2)
                res2 = res1 * x
                return res1 * res2
            else:
                res = mypositivepow(x, n // 2)
                return res ** 2

        return mypositivepow(x, n) if n >= 0 else mypositivepow(1 / x, -n)


x = 2
n = 3
res = Solution().myPow(x, n)
print(res)
