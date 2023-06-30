"""
author:wjw
分析：很简单，分析个屁
"""


class Solution:
    def reverse(self, x):
        if x==0:
            return 0
        if x > 0:
            sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        result = 0
        while (x != 0):
            y = x % 10

            result = result * 10 + y
            x = x // 10
        if sign * result > 2 ** 31 - 1 or sign * result < -2 ** 31:
            return 0
        return sign * result


x = 120
s = Solution()

print(s.reverse(x))
