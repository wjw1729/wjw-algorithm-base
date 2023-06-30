"""
author:wjw
分析：改题目的主要难点在于高次幂取模算法，此处使用了蒙哥马利算法。
"""


def get_mod(a, b, c):
    res = 1
    temp = a
    while b > 0:
        if b & 1:
            res = (res * temp) % c
        temp = (temp * temp) % c
        b >>= 1
    return res


class Solution:
    def countGoodNumbers(self, n):
        odd = n // 2
        even = (n + 1) // 2

        mod1 = get_mod(5, even, 10 ** 9 + 7)
        mod2 = get_mod(4, odd, 10 ** 9 + 7)

        return (mod1 * mod2) % (10 ** 9 + 7)


n = 1
n=50
res = Solution().countGoodNumbers(n)
print(res)
