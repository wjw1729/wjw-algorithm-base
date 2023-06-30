"""
author:wjw
分析；RB算法
时间复杂度:O(n)
"""


class Solution:
    def shortestPalindrome(self, s):
        base = 131
        MOD = 10 ** 9 + 7
        n = len(s)

        hashvalue = [0] * n
        rshashvalue = [0] * n

        for i in range(n):
            mult = pow(base, i, MOD)
            hashvalue[i] = (hashvalue[i - 1] * base + ord(s[i]) - ord('a')) % MOD
            rshashvalue[i] = (rshashvalue[i - 1] + (ord(s[i]) - ord('a')) * mult) % MOD

            if hashvalue[i] == rshashvalue[i]:
                maxindex = i

        return s[maxindex + 1:][::-1] + s


s = "bbcecbbb"
s = "abcd"
res = Solution().shortestPalindrome(s)
print(res)
