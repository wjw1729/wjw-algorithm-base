"""
author:wjw
分析：偶数好处理+奇数：前缀+后缀.pre[i][0]、pre[i][1]表示s[0:i]满足以0或1结尾的前缀字符串，suf[i][0],suf[i][1]表示s[i:]满足以0或1开头的字符串
"""


def exp_func(a, b):
    if a == b:
        return 1
    else:
        return 0


class Solution:
    def minFlips(self, s):
        n = len(s)

        pre = [[0, 0] for i in range(n)]
        suf = [[0, 0] for i in range(n)]

        if n % 2 == 0:
            a = '01' * (n // 2)
            b = '10' * (n // 2)

            ans = min(bin(int(s, base=2) ^ int(a, base=2)).count('1'), bin(int(s, base=2) ^ int(b, base=2)).count('1'))

        else:
            for i in range(n):
                if i == 0:
                    pre[0][0] = exp_func(int(s[0]), 1)
                    pre[0][1] = exp_func(int(s[0]), 0)
                    continue
                pre[i][0] = pre[i - 1][1] + exp_func(int(s[i]), 1)
                pre[i][1] = pre[i - 1][0] + exp_func(int(s[i]), 0)

            for i in range(n - 1, -1, -1):
                if i == n - 1:
                    suf[i][0] = exp_func(int(s[i]), 1)
                    suf[i][1] = exp_func(int(s[i]), 0)
                    continue
                suf[i][0] = suf[i + 1][1] + exp_func(int(s[i]), 1)
                suf[i][1] = suf[i + 1][0] + exp_func(int(s[i]), 0)

            ans = min(pre[n - 1][0], pre[n - 1][1])

            for i in range(n - 1):
                ans = min(ans, pre[i][0] + suf[i + 1][0])
                ans = min(ans, pre[i][1] + suf[i + 1][1])

        return ans


s = "010"
res = Solution().minFlips(s)
print(res)
