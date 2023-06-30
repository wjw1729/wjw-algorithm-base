"""
author:wjw
分析：判断一个数是否是完全平方数？sqrt(c-a**2)是否为整数
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        bound = int(math.sqrt(c))
        for i in range(0, bound + 1):
            b = math.sqrt(c - i ** 2)
            if b % 1 == 0:
                return True

        return False


c = 1
res = Solution().judgeSquareSum(c)
print(res)
