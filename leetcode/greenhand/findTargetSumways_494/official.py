"""
author:wjw
分析：dp[i][j]表示到第i个nums数，和为j的总取法数。问题转化为在nums中选出和为positive的数目。
"""


class Solution:
    def findTargetSumWays(self, nums, target):

        n = len(nums)
        nums_sum = sum(nums)

        if (nums_sum + target) % 2 or target>nums_sum:
            return 0
        positive = (nums_sum + target) // 2  # 问题转化为在nums中选出和为positive的数目。

        dp = [[0 for i in range(positive + 1)] for i in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(positive + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][positive]


nums = [1, 1, 1, 1, 1]
# nums = [1]
target = 3
res = Solution().findTargetSumWays(nums, target)
print(res)
