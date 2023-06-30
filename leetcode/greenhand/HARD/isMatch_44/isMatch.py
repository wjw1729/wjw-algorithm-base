"""
author:wjw
分析：动态规划。dp[i][j]表示s中长度为i的字符子串是否与p中长度为j的子串匹配。
"""


def isequal(s1, s2):
    if s1 == s2 or s2 == '?':
        return True
    else:
        return False


class Solution:
    def isMatch(self, s, p):
        n1 = len(s)
        n2 = len(p)

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if j == 0:
                    if i == 0:
                        dp[i][j] = True
                    continue
                if i == 0:
                    if p[:j] == '*'*j:
                        dp[i][j] = True
                    continue

                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j-1]
                elif isequal(s[i - 1], p[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]


s = "aa"
p = "*"
"""
s = "cb"
p = "?a"

s = "adceb"
p = "*a*b"
s = "acdcb"
p = "a*c?b"
"""
res = Solution().isMatch(s, p)
print(res)
