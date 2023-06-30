"""
author:wjw
分析：滚动数组优化
"""


class Solution():
    def isInterleave(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if (n1 + n2) != n3:
            return False
        dp = [False] * (n2 + 1)

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0:
                    dp[j] = (s2[:j] == s3[:j])
                    continue
                if j == 0:
                    dp[j] = (s1[:i] == s3[:i])
                    continue
                dp[j] = (dp[j] & (s1[i - 1] == s3[i + j - 1])) or (dp[j - 1] & (s2[j - 1] == s3[i + j - 1]))

        return dp[-1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
res = Solution().isInterleave(s1, s2, s3)
print(res)
