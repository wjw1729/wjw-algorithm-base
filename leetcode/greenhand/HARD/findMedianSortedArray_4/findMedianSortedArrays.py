"""
author:wjw
分析：
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        return nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[n // 2]) / 2


nums1 = [1, 3]
nums2 = [2, 2]
res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)
