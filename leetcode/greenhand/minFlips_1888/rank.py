"""
author:wjw
分析：公式的实际意义？
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        zeros1 = s[::2].count('0')
        zeros2 = s[1::2].count('0')
        m = n // 2
        if n % 2 == 0:
            return min(zeros1 + m - zeros2, zeros2 + m - zeros1)
        ans = min(zeros1 + m - zeros2, zeros2 + m + 1 - zeros1)
        for i in range(n-1):
            zeros1, zeros2 = zeros2, zeros1
            if s[i] == '0':
                zeros1 += 1
                zeros2 -= 1
            ans = min(ans, zeros1 + m - zeros2, zeros2 + m + 1 - zeros1)
        return ans