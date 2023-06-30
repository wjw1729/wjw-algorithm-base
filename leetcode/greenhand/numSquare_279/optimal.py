"""
author:wjw
分析：四平方和定理。数论啊，爷的最爱
"""
import math


class Solution:
    def numSquare(self, n):

        n_copy = n
        while n_copy % 4 == 0:
            n_copy //= 4

        if n_copy % 8 == 7:
            return 4
        else:
            if math.sqrt(n) % 1 == 0:
                return 1
            for i in range(math.floor(math.sqrt(n)) + 1):
                if math.sqrt(n - i ** 2) % 1 == 0:
                    return 2

            return 3


n = 1
res = Solution().numSquare(n)
print(res)
