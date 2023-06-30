"""
author:wjw
分析:dp[i][j]表示s1[:i]和s2[:j]能否交错构成s[:i+j]
"""


class Solution:
    def isInterleave(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if (n1 + n2) != n3:
            return False
        dp = [[False] * (n2 + 1) for i in range(n1 + 1)]

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0:
                    dp[i][j] = (s3[:j] == s2[:j])
                    continue
                if j == 0:
                    dp[i][j] = (s3[:i] == s1[:i])
                    continue
                dp[i][j] = (dp[i - 1][j] & (s1[i - 1] == s3[i + j - 1])) or (
                            dp[i][j - 1] & (s2[j - 1] == s3[i + j - 1]))

        return dp[n1][n2]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
s1 = ""
s2 = ""
s3 = ""
res = Solution().isInterleave(s1, s2, s3)
print(res)
