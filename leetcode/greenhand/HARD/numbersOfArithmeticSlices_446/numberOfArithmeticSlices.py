"""
author:wjw
分析：动态规划+哈希表。
时间复杂度：O(n**2)
"""

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        ans = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d] + 1
                ans += dp[j][d]
        return ans


nums = [2, 4, 6, 8, 10]
#nums = [7, 7, 7, 7, 7]
res = Solution().numberOfArithmeticSlices(nums)
print(res)
