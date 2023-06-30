"""
author:wjw
分析：dp[i]表示在0-i区间上能够跳到对额最远位置
"""


class Solution:
    def canJump(self, nums):
        n = len(nums)
        dp = [0] * n

        for i in range(n):

            if dp[i - 1] >= i or i == 0:
                dp[i] = max(dp[i - 1], i + nums[i])

            if dp[i] >= n - 1:
                return True
        return False


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
nums = [2, 5, 0, 0]
nums=[1,2,3]
res = Solution().canJump(nums)
print(res)
