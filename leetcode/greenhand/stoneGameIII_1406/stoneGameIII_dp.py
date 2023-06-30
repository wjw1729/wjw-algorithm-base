"""
author:wjw
分析：dp[i]表示当前选手在从i开始的堆中进行挑选所能达到的最大分差。（在每次递推之间，当前选手的概念会进行交换。）开始时分差为0，dp[n]=0
"""


class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        dp = [float('-inf')] * n + [0]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, i + 4):
                if j <= n:
                    dp[i] = max(dp[i], sum(stoneValue[i:j]) - dp[j])

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] == 0:
            return 'Tie'
        else:
            return 'Bob'


values = [1, 2, 3, 7]
"""
values = [1, 2, 3, -9]
values = [1, 2, 3, 6]
values = [1, 2, 3, -1, -2, -3, 7]
values = [-1, -2, -3]
"""
res = Solution().stoneGameIII(values)
print(res)
