"""
author:wjw
分析：递归来做,递归深度太深了，出错
"""


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob(nums[1:len(nums) - 2]) + nums[-1], self.rob(nums[:len(nums) - 1]))


l = [1, 3, 1, 3, 100]
s = Solution()
result = s.rob(l)
print(result)
