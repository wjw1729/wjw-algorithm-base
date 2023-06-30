"""
author:wjw
分析:不能用乘法、除法、mod运算符，所以回归本质->辗转相除法haha,遇到大数时间复杂度会很高，所以考虑将被除数化为字符串，分块运算,将l1中的字符取出依次进行计算，计算结果保存在res列表中，最后合并即可。
优化：移位？
"""

import time


def zhanzhuan(dividend, divisor):
    ans = 0
    while divisor <= dividend:
        dividend = dividend - divisor
        ans += 1
    return (ans, dividend)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            sign = 1
            divisor = abs(divisor)
            dividend = abs(dividend)

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
            divisor = abs(divisor)
            dividend = abs(dividend)

        s1 = str(dividend)
        l1 = list(s1)
        n = len(l1)
        pop_num = 0
        operator = '0'
        res = []
        while pop_num < n:
            operator += l1.pop(0)
            pop_num += 1
            a, b = zhanzhuan(int(operator), divisor)
            res.append(str(a))
            operator = str(b)

        ans = '0'
        for i in range(len(res)):
            ans += res[i]

        ans = int(ans) * sign
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 2 ** 31 - 1
        return ans


t1 = time.time()
dividend = -7
divisor = 3
res = Solution().divide(dividend, divisor)
print(res)
print(time.time() - t1)
