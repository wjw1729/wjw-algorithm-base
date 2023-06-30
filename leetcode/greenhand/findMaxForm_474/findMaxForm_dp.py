"""
author:wjw
分析；dp[i][j][k]表示在到第i-1个字符串，用j个0和k个1能选出来的最大子集数.
"""


class Solution:
    def findMaxForm(self, strs, m, n):
        strs_n = len(strs)
        dp = [[[0 for i in range(n + 1)] for i in range(m + 1)] for i in range(strs_n + 1)]
        for i in range(strs_n + 1):

            num_0 = strs[i - 1].count('0')
            num_1 = strs[i - 1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):

                    if i == 0:
                        dp[i][j][k] = 0
                        continue

                    if num_0 <= j and num_1 <= k:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - num_0][k - num_1] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[strs_n][m][n]


strs = ["10", "0001", "111001", "1", "0"]
#strs = ["111", "1000", "1000", "1000"]
m = 5
n = 3
res = Solution().findMaxForm(strs, m, n)
print(res)
