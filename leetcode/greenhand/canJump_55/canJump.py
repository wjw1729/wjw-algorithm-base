"""
author；wjw
分析：用dp[i]表示能否到达i处。
"""


class Solution:
    def canJump(self, nums):

        if min(nums) > 0:
            return True

        dp = [False] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[0] = True

            if dp[i] == True:
                dp[i + 1:i + nums[i] + 1] = [True] * nums[i]

        return dp[len(nums) - 1]


nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
res = Solution().canJump(nums)
print(res)
