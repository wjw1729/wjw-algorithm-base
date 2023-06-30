"""
author:wjw
分析：
"""

from collections import Counter


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        CM_num = s.count('CM')
        ans += CM_num * 900
        s = s.replace('CM', '')

        CD_num = s.count('CD')
        ans += CD_num * 400
        s = s.replace('CD', '')

        XC_num = s.count('XC')
        ans += XC_num * 90
        s = s.replace('XC', '')

        XL_num = s.count('XL')
        ans += XL_num * 40
        s = s.replace('XL', '')

        IX_num = s.count('IX')
        ans += IX_num * 9
        s = s.replace('IX', '')

        IV_num = s.count('IV')
        ans += IV_num * 4
        s = s.replace('IV', '')

        d = Counter(s)

        ans += d['I'] + d['V'] * 5 + d['X'] * 10 + d['L'] * 50 + d['C'] * 100 + d['D'] * 500 + d['M'] * 1000

        return ans


s = 'MCMXCIV'
res = Solution().romanToInt(s)
print(res)
