"""
author:wjw
分析：dp[i][j]表示当数组剩下部分为i到j时，即在下标范围[i,j]中，当前玩家与另外一个玩家的分数之差的最大值。当前玩家不一定是先手玩家。

"""


class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1]


nums = [1, 5, 2]
nums = [1, 5, 233, 7]
res = Solution().predictTheWinner(nums)
print(res)
