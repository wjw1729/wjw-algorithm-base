"""
author:wjw
分析：
"""

from collections import Counter


class Solution:
    def singleNumber(self, nums):
        d = Counter(nums)
        for k, v in d.items():
            if v == 1:
                return k


nums = nums = [2, 2, 3, 2]
nums = [0, 1, 0, 1, 0, 1, 99]
res = Solution().singleNumber(nums)
print(res)
