"""
author:wjw
分析：该问题可以转换为第一类斯特林数。
时间复杂度:O(n*k)
"""


class Solution:
    def rearrangeSticks(self, n, k):
        MOD = 10 ** 9 + 7
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(k + 1, i + 1)):
                f[i][j] = (f[i - 1][j - 1] + (i - 1) * f[i - 1][j]) % MOD

        return f[n][k]


n = 11
k = 1
res = Solution().rearrangeSticks(n, k)
print(res)
