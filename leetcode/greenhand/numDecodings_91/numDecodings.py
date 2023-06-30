"""
author:wjw
分析：动态规划，状态转移方程。正确的思路，因该先将含0的情况分析清楚，再在此基础上推导状态转移方程，以及边界条件。
"""


class Solution:
    def numDecodings(self, s):
        illegal = ['00', '30', '40', '50', '60', '70', '80', '90']
        for i in illegal:
            if i in s:
                return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        dp = [0] * len(s)
        dp[0] = 1
        if int(s[0:2]) <= 26 and int(s[0:2]) >= 1 and s[1] != '0':
            dp[1] = 2
        else:
            dp[1] = 1

        if s[1] == '0':
            dp[2] = 1
        elif int(s[2 - 1:2 + 1]) >= 1 and int(s[2 - 1:2 + 1]) <= 26:
            if s[2] != '0':
                dp[2] = dp[2 - 1] + dp[2 - 2]
            else:
                dp[2] = dp[2 - 2]
        else:
            dp[2] = dp[2 - 1]

        for i in range(3, len(s)):
            if s[i-1] == '0':
                dp[i] = dp[i - 3]
            elif int(s[i-1:i+1]) >= 1 and int(s[i-1:i+1]) <= 26:
                if s[i] != '0':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[len(s) - 1]


s = '20712323131111111111111111111212'
s=''
result = Solution().numDecodings(s)
print(result)
