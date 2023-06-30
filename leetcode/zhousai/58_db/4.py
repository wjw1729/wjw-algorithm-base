"""
author:wjw
分析：manacher算法+位置分割。
时间复杂度O(n).
"""


class Solution:
    def maxProduct(self, s):
        d1 = []
        l = 0
        r = -1
        n = len(s)

        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)

            while i > r and 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1.append(k)
            if i + k - 1 > r:
                l = i - k + 1
                r = l + k - 1

        pre, suf = [0] * n, [0] * n

        for i in range(n):
            pre[i + d1[i] - 1] = max(pre[i + d1[i] - 1], d1[i] * 2 - 1)
            suf[i - d1[i] + 1] = max(suf[i - d1[i] + 1], d1[i] * 2 - 1)

        for i in range(1, n):
            pre[i] = max(pre[i], pre[i - 1])

        for i in range(n - 2, -1, -1):
            pre[i] = max(pre[i], pre[i + 1] - 2)

        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i], suf[i + 1])
        for i in range(1, n):
            suf[i] = max(suf[i], suf[i - 1] - 2)

        ans = max([pre[i] * suf[i + 1] for i in range(n - 1)])

        return ans


s = "ababbb"
s = "zaaaxbbby"
res = Solution().maxProduct(s)
print(res)
