"""
author:wjw
分析：
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        xor = bin(xor)
        ans = xor.count('1')
        return ans


x = 1
y = 4
res = Solution().hammingDistance(x, y)
print(res)
