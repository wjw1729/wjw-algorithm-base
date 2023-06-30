"""
author:wjw
分析：该实现方法使用了递归，需占用大量的内存资源
"""


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            res = max(self.rob(nums[:len(nums) - 2]) + nums[-1], self.rob(nums[:len(nums) - 1]))
            return res


l = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
s = Solution()
result = s.rob(l)
print(result)
