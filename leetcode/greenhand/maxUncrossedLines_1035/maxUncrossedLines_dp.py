"""
author:wjw
分析：最长公共子序列。动态规划.dp[i][j]表示nums1长度为i和nums2[0:]长度为j的最长公共子序列长度。
"""


class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue

                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
nums1 = [2, 5, 1, 2, 5]
nums2 = [10, 5, 2, 1, 5, 2]
nums1 = [1, 3, 7, 1, 7, 5]
nums2 = [1, 9, 2, 5, 1]
res = Solution().maxUncrossedLines(nums1, nums2)
print(res)
