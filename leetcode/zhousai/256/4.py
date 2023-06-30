"""
author:wjw
分析：动态规划.
时间复杂度:O(n)
"""
class Solution:
    def numberOfUniqueGoodSubsequence(self, s):
        dp0 = 0
        dp1 = 0
        has0 = 0
        MOD = 10 ** 9 + 7

        for ch in s[::-1]:
            if ch == "0":
                has0 = 1
                dp0 = (dp0 + dp1 + 1) % MOD
            else:
                dp1 = (dp0 + dp1 + 1) % MOD

        return (dp1 + has0) % MOD


s = "001"
s = "11"
s = "101"
res = Solution().numberOfUniqueGoodSubsequence(s)
print(res)
