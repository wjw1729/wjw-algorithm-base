"""
author:wjw
分析：二分搜索
"""


class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:

            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid

            elif nums[mid] < nums[right]:
                right = mid
            if right - left == 1:
                return nums[right]


nums = [3, 4, 5, 1, 2]
nums = [1]
res = Solution().findMin(nums)
print(res)
