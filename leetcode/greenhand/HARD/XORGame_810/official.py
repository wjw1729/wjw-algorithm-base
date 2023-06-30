"""
official:官方分析需要一定的思维证明，仅在长度为偶数or异或和为0的情况下，Alice才赢   
"""
from functools import reduce


class Solution:
    def xorGame(self, nums):
        if len(nums) % 2 == 0:
            return True

        xorsum = reduce(lambda x, y: x ^ y, nums)
        return xorsum == 0


nums = [1, 1, 2]
res = Solution().xorGame(nums)
print(res)
