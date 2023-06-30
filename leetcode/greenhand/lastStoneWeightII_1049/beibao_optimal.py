"""
author:wjw
分析：背包问题+动态规划+规划优化
"""


class Solution:
    def beibao(self, nums, target):
        n = len(nums)
        dp = [0 for i in range(target + 1)]

        for i in range(1, n + 1):
            for j in range(target,-1,-1):
                if nums[i - 1] <= j:
                    dp[j] = max(dp[j], dp[j - nums[i - 1]] + nums[i - 1])

        return dp[target]


nums = [1, 1, 1, 2, 3, 4, 5, 6]
target = 10
res = Solution().beibao(nums, target)
print(res)
