"""
author:wjw
分析：二分法.
    Frequency2k(nums, f)返回将最大词频改为f次的最小操作次数mink.
"""


class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        n = len(nums)

        def Frequency2k(nums, f):
            nums.sort()
            k = sum([nums[f - 1] - nums[j] for j in range(f)])
            mink = k

            for i in range(1, n - f + 1):
                k = k - (nums[i + f - 2] - nums[i - 1]) + (nums[i + f - 1] - nums[i + f - 2]) * (f - 1)
                mink = min(k, mink)
            return mink

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if Frequency2k(nums, mid) > k:
                right = mid - 1
            else:
                left = mid
            if right - left == 1:
                print(Frequency2k(nums, right), right)
                return right if Frequency2k(nums, right) <= k else left

        # print(1)
        return left
