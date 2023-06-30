"""
author:wjw
分析：按位进行统计。
"""


class Solution:
    def countDigitOne(self, n):
        num = str(n)
        length = len(num)
        ans = 0

        for i in range(length - 1, -1, -1):
            pre = int(num[:i]) + 1 if i != 0 else 1

            if int(num[i]) > 1:
                ans += pre * (10 ** (length - 1 - i))
            elif int(num[i]) == 1:
                if i != length - 1:
                    ans += (pre - 1) * (10 ** (length - 1 - i)) + int(num[i + 1:]) + 1
                else:
                    ans += (pre - 1) * (10 ** (length - 1 - i)) + 1
            else:
                ans += (pre - 1) * (10 ** (length - 1 - i))

        return ans


n = 0
res = Solution().countDigitOne(n)
print(res)
