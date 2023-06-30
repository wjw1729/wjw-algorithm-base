"""
author:wjw
分析:动态规划。dp[i][j]表示到i个nums时，和为j-1000的不同表达式数目。i的范围0-len（nums）,j:[0,2000].
由于sum有负值，所以整体值域平移1000
"""


class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        dp = [[0 for i in range(2001)] for i in range(n + 1)]

        dp[0][1000] = 1
        for i in range(1, n + 1):
            for j in range(2001):
                if 0 <= j - nums[i - 1] <= 2000 and 0 <= j + nums[i - 1] <= 2000:

                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
                    continue
                elif 0 <= j - nums[i - 1] <= 2000:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
                    continue
                elif 0 <= j + nums[i - 1] <= 2000:
                    dp[i][j] = dp[i - 1][j + nums[i - 1]]
                    continue

        return dp[n][target + 1000]


nums = [1, 1, 1, 1, 1]
nums = [1]
target = 1
res = Solution().findTargetSumWays(nums, target)
print(res)
