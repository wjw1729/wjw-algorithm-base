"""

author:wjw
分析：此处dp[i]变为3中dp[i]的前缀和。
"""


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit) -> int:
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        dp = [0] * n
        dp[0] = 2

        for i in range(1, n):
            k = nextVisit[i]

            dp[i] = 2 + 2 * dp[i - 1] - (dp[k - 1] if k > 0 else 0)
            dp[i] %= MOD

        return dp[n - 2]


nextVisit = [0, 1, 2, 0]
res = Solution().firstDayBeenInAllRooms(nextVisit)
print(res)
