"""
authtor:wjw
分析：动态规划。
时间复杂度：O(n**2)
"""


class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)

        dp = [[0] * n for _ in range(n)]


        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


s = "bbbab"
s = 'cbbd'
res = Solution().longestPalindromeSubseq(s)
print(res)
