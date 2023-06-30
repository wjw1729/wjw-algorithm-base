"""
author:wjw
分析：

"""


class Solution:
    def numberOfCombinations(self, num):
        MOD = 10 ** 9 + 7

        n = len(num)
        dp = [[0] * n for _ in range(n)]

        lcp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def less(l1, l2, r2):
            l = lcp[l1][l2]
            return l >= r2 - l2 or num[l1 + l] < num[l2 + l]

        dp[0] = [1] * n

        for i in range(1, n):
            if num[i] == '0':
                continue
            presum = 0
            k = i - 1
            for j in range(i, n):

                dp[i][j] = presum
                if k < 0:
                    continue
                if num[k] > '0' and less(k, i, j + 1):
                    dp[i][j] = (dp[i][j] + dp[k][i - 1]) % MOD
                presum = (presum + dp[k][i - 1]) % MOD
                k -= 1

        ans = sum(dp[i][n - 1] for i in range(n)) % MOD
        return ans


num = '327'
num = "9" * 1000
res = Solution().numberOfCombinations(num)
print(res)
