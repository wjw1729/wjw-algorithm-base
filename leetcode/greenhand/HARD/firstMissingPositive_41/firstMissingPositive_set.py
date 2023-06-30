"""
author:wjw
分析：
"""

class Solution:
    def firstMissingPostive(self,nums):
        nums=set(nums)

        for i in range(1,2**31):
            if i not in nums:
                return i