"""
author:wjw
分析：先将list排序，然后通过一个window窗口进行移动，判断两遍数的异或值是否为最大。
"""


class Solution:
    def findMaximumXOR(self, nums):
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        maxXor = 0
        while left < right:

            x0 = nums[left] ^ nums[right]
            x1 = nums[left + 1] ^ nums[right]
            x2 = nums[left] ^ nums[right - 1]

            if x2 >= x1:
                right = right - 1

            if x1 > x2:
                left = left + 1

            maxXor = max(maxXor, x0, x1, x2)
        return maxXor


nums = [3, 10, 5, 25, 2, 8]
nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
nums=[20,12,29,76,94,65,95,33,79,80,57,78]
res = Solution().findMaximumXOR(nums)
print(res)
