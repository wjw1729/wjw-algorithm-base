"""
author：wjw
分析：熟练的运用itertools和reduce.
"""
import itertools
from functools import reduce


class Solution:
    def subsetXORSum(self, nums):

        ans = 0
        n = len(nums)
        for i in range(1, n + 1):
            numls = list(itertools.combinations(nums, i))
            for comb in numls:
                ans += reduce(lambda x, y: x ^ y, comb)

        return ans


nums =[5,1,6]
res = Solution().subsetXORSum(nums)
print(res)
