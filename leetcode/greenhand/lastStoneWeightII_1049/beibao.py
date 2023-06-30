"""
author:wjw
分析：背包问题从nums，中尽可能的选出target内的最大数量。
    dp[i][total]表示到nums[i-1]能够选出的不超过total的最大数量
"""


class Solution:
    def beibao(self, nums, target):
        n = len(nums)

        dp = [[0 for i in range(target + 1)] for i in range(n+1)]

        for i in range(1, n + 1):
            for j in range(target + 1):
                if nums[i-1]<=j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i-1]] + nums[i - 1])
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][target]


nums=[1,1,1,2,3,4,5,6]
target=10
res=Solution().beibao(nums,target)
print(res)

