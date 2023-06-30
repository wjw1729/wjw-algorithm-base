"""
author:wjw
分析：dp[i]=dp[i]| (not dp[i-j**2]) <==>  any(dp[i-j**2]) dp[i]==True
"""

import time
class Solution:
    def winnerSquareGame(self, n):

        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, int(pow(i, 0.5) + 1)):
                if not dp[i - j ** 2]:
                    dp[i] = True
                    break
        return dp[n]

t1=time.time()
n = 1000
res = Solution().winnerSquareGame(n)
print(res)
print(time.time()-t1)