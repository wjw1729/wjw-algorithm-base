"""
author:wjw
分析：还比较简单吧。。。。。
"""


class Solution:
    def removeDuplicates(self, nums):

        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                nums.pop(i + 1)
            else:
                i = i + 1
        return len(nums)


nums = [1, 1, 2]
S = Solution()
res = S.removeDuplicates(nums)
print(res)
