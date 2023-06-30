"""
author:wjw
分析：
"""
import itertools
import time


class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))


t1 = time.time()
nums = [1, 2, 3, 4, 5, 6]
res = Solution().permute(nums)
print(res)
print(time.time() - t1)
