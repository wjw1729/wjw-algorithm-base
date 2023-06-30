"""
author:wjw
分析：动态规划！第28行的状态转移方程比较重要（难搞！）！
"""


class Solution:
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)

        dp = [[False] * (len_p + 1) for i in range(len_s + 1)]

        dp[0][0] = True

        for i in range(0, len_s + 1):
            for j in range(1, len_p + 1):
                if i == 0:
                    if p[j - 1] == '*':
                        dp[i][j] = dp[i][j - 2]
                    continue

                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    continue
                if p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j - 2]

        return dp[-1][-1]


s = "aa"
p = "a"
s = "aab"
p = "c*a*b"
s = "aaa"
p = "ab*a*c*a"
res = Solution().isMatch(s, p)
print(res)
