"""
author:wjw
分析：字符串模拟乘法。
"""


class Solution:
    def multuiply(self, num1, num2):
        m, n = len(num1), len(num2)

        ans = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i + j + 1] += int(num1[i]) * int(num2[j])
                if ans[i + j + 1] >= 10:
                    ans[i + j] += ans[i + j + 1] // 10
                    ans[i + j + 1] %= 10
        """
        for i in range(m + n - 1, -1, -1):
            if ans[i] >= 10:
                ans[i - 1] += ans[i] // 10
                ans[i] %= 10
        """
        ans = ''.join([str(x) for x in ans])

        return ans if ans[0] != '0' else ans[1:]


num1 = '2'
num2 = '3'
num1 = '123'
num2 = '456'
res = Solution().multuiply(num1, num2)
print(res)
