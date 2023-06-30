"""
author:wjw
fenxi:dongtaiguihua.
"""

class Solution:
    def maxProfit(self, k: int, prices) -> int:

        n = len(prices)
        buy = [[float("-inf")] * (1 + k) for _ in range(n)]
        sell = [[float("-inf")] * (k + 1) for _ in range(n)]

        buy[0][0] = -prices[0]
        sell[0][0] = 0

        for i in range(1, n):
            for j in range(k+1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], (buy[i - 1][j-1] if j>0 else float('-inf')) + prices[i])

        return max(sell[n - 1])

k=2

prices=[3,3,5,0,0,3,1,4]
res=Solution().maxProfit(k,prices)
print(res)