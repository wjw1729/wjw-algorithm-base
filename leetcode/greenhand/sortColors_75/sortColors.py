"""
author:wjw
分析：
"""


class Solution:
    def sortColors(self, nums):
        nums.sort()
        return nums


nums = [2, 0, 2, 1, 1, 0]
res = Solution().sortColors(nums)
print(res)
