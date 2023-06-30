"""
author:wjw
分析：问题转化+动态规划+剪枝+动态规划降维

"""


class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        nums_sum = sum(nums)

        if (nums_sum + target) % 2 or target > nums_sum:
            return 0

        positive = (nums_sum + target) // 2

        dp = [0 for i in range(positive + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(positive, -1, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] + dp[j - nums[i - 1]]

        return dp[-1]


nums = [1, 1, 1, 1, 1]
# nums = [1]
target = 3
res = Solution().findTargetSumWays(nums, target)
print(res)
