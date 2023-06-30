"""
author:wjw
分析：
"""


class Solution:
    def countArrangement(self, n):
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count('1')

            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]

        return f[(1 << n) - 1]


n = 15
res = Solution().countArrangement(n)
print(res)
