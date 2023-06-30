"""
author:wjw
分析：动态规划，但是要分配数组存储变量，好像有点慢！
"""


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        dp = [float('inf')] * n
        dp[0] = 1
        m = len(primes)
        p = [0] * m
        nums = [0] * m

        for i in range(1, n):
            for j in range(m):
                nums[j] = dp[p[j]] * primes[j]
                dp[i] = min(dp[i], nums[j])

            for j in range(m):
                if dp[i] == nums[j]:
                    p[j] += 1

        return dp[-1]


n = 12
primes = [2, 7, 13, 19]
res = Solution().nthSuperUglyNumber(n, primes)
print(res)
