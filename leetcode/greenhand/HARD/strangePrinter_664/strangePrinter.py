"""
author:wjw
分析：dp[i]表示str(i)及前面字符时的最少打印次数
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(len(s)):
            if i == 0:
                dp[0] = 1
                continue

            if s[i] == s[i - 1] or s[i] == s[0]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp[len(s) - 1]


s = 'abab'
res = Solution().strangePrinter(s)
print(res)
