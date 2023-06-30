"""
author:wjw
分析:动态规划+哈希表。
    时间复杂度:O（n）
    和446类似.
"""

from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j][d] + 1
                ans = max(ans, dp[i][d])

        return ans + 1


nums = [2, 4, 6, 8, 10]
nums=[7,7,7,7,7]
res = Solution().longestArithSeqLength(nums)
print(res)
