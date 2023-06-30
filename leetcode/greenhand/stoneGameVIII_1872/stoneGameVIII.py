"""
author:wjw
分析：dp[i]表示选择者在剩下的[i,n)的前缀和中选择所能达到的最大差值。
"""


class Solution:
    def stoneGameVIII(self, stones):

        n = len(stones)
        dp = [0] * n

        presum = []
        total = 0
        for stone in stones:
            total += stone
            presum.append(total)


        for i in range(n - 1, 0, -1):
            if i == n - 1:
                dp[i] = presum[i]
            else:
                dp[i] = max(presum[i] - dp[i + 1], dp[i + 1])

        return dp[1]


stones = [-1, 2, -3, 4, -5]
stones = [7,-6,5,10,5,-2,-6]
stones = [-10,-12]
res = Solution().stoneGameVIII(stones)
print(res)
