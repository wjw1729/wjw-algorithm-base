"""
author:wjw
分析：区间dp.动态规划+预处理。dp[i][j]表示将nums[:i+1]分为j段的总内存损耗。
状态转移方程：dp[i][j]=min(dp[i0-1][j-1]+g[i0][i])
"""


class Solution:
    def minSpaceWastedKResizing(self, nums, k: int) -> int:

        n = len(nums)
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        g = [[0] * n for _ in range(n)]

        total = 0
        presum = [0] * (n + 1)
        for i in range(n):
            total += nums[i]
            presum[i + 1] = total
            best = 0
            for j in range(i, -1, -1):
                best = max(best, nums[j])
                g[j][i] = best * (i - j + 1) - (presum[i + 1] - presum[j])

        for i in range(n):
            for j in range(1, k + 2):
                for m in range(i+1):
                    dp[i][j] = min(dp[i][j], (0 if m == 0 else dp[m - 1][j - 1]) + g[m][i])

        return dp[n - 1][k + 1]


nums = [10, 20]
k = 0

nums = [10,20,30]
k = 1

nums = [10, 20, 15, 30, 20]
k = 2
"""
nums = [2, 48, 18, 16, 15, 9, 48, 7, 44, 48]
k = 1
"""
res = Solution().minSpaceWastedKResizing(nums, k)
print(res)
