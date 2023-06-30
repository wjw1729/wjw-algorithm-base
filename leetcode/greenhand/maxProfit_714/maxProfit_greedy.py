"""
author:wjw
分析：贪心算法。当我们卖出一支股票时，我们就立即获得了以相同价格并且免除手续费买入一支股票的权利。
"""


class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        buy = prices[0] + fee
        profit = 0

        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]

        return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2

prices = [1, 3, 7, 5, 10, 3]
fee = 3

res = Solution().maxProfit(prices, fee)
print(res)
