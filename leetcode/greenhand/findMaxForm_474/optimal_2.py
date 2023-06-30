"""
author:wjw
分析：对于m和n的遍历反向，即可省去另一个空间的需求。
"""


class Solution:
    def findMaxForm(self, strs, m, n):
        strs_n = len(strs)
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for i in range(1, strs_n + 1):
            nums_0 = strs[i - 1].count('0')
            nums_1 = strs[i - 1].count('1')

            for j in range(m, nums_0 - 1, -1):
                for k in range(n, nums_1 - 1, -1):

                    if nums_0 <= j and nums_1 <= k:
                        dp[j][k] = max(dp[j][k], dp[j - nums_0][k - nums_1] + 1)

        return dp[m][n]


strs = ["10", "0001", "111001", "1", "0"]
# strs=["111","1000","1000","1000"]
m = 5
n = 3
res = Solution().findMaxForm(strs, m, n)
print(res)
