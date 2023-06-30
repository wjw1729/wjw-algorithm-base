"""
author；wjw
分析：用dp[i]表示能否到达i处。
"""


class Solution:
    def canJump(self, nums):
        
        n=len(nums)
        # if min(nums) > 0:
        #     return True

        for i in range(n-1):
            nums[i]=i+nums[i]
        i=0
        while i<n:
            if max(nums[i:nums[i]])>=n-1:
               return True
            else:
                i=nums[i]


nums = [2, 3, 1, 1, 4]
#nums = [3, 2, 1, 0, 4]
res = Solution().canJump(nums)
print(res)
