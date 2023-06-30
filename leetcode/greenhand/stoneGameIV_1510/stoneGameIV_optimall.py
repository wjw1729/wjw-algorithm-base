"""
author:wjw
分析：
"""
import time


class Solution:
    def winnerSquareGame(self, n):

        dp = [False] * (n + 1)

        x = [i * i for i in range(1, int(pow(n, 0.5) + 1))]
        check = False
        for i in range(n + 1):
            for j in x:
                if not dp[i]:
                    if i + j > n:
                        break
                    dp[i + j] = True
                    if i + j == n:
                        check = True
            if check:
                break

        return dp[n]


t1 = time.time()
n = 1000
res = Solution().winnerSquareGame(n)
print(res)
print(time.time() - t1)
