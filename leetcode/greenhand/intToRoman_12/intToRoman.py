"""
author:wjw
分析:按照规则来，就行了
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        M_num = num // 1000
        ans += 'M' * M_num

        num = num % 1000
        CM_num = num // 900
        ans += 'CM' * CM_num

        num = num % 900
        D_num = num // 500
        ans += 'D' * D_num

        num = num % 500
        CD_num = num // 400
        ans += 'CD' * CD_num

        num = num % 400
        C_num = num // 100
        ans += 'C' * C_num

        num = num % 100
        XC_num = num // 90
        ans += 'XC' * XC_num

        num = num % 90
        L_num = num // 50
        ans += 'L' * L_num

        num = num % 50
        XL_num = num // 40
        ans += 'XL' * XL_num

        num = num % 40
        X_num = num // 10
        ans += 'X' * X_num

        num = num % 10
        IX_num = num // 9
        ans += 'IX' * IX_num

        num = num % 9
        V_num = num // 5
        ans += 'V' * V_num

        num = num % 5
        IV_num = num // 4
        ans += 'IV' * IV_num

        num = num % 4
        I_num = num // 1
        ans += 'I' * I_num

        return ans


num = 40
res = Solution().intToRoman(num)
print(res)
