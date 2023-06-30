"""
author:wjw
分析：
"""

import bisect


class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        index_left = bisect.bisect_left(nums, target)
        index_right = bisect.bisect(nums, target)

        return [index_left, index_right - 1]


nums = [5, 7, 7, 8, 8, 10]
target = 11
res = Solution().searchRange(nums, target)
print(res)
