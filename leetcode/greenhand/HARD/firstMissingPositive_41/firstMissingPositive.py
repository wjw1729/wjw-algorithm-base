"""
author:wjw
分析：内存没有小很多，还慢，建议用哈希表（集合）。
"""


class Solution:
    def firstMissingPositive(self, nums):

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num=abs(nums[i])
            if n >= num > 0:
                nums[num - 1] = -nums[num - 1]

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n+1


nums = [0, 1, 2]
nums=[3,4,2,1]
res = Solution().firstMissingPositive(nums)
print(res)
