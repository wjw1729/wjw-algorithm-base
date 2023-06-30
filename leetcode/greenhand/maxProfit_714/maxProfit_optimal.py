"""
author:wjw
分析：

"""

class Solution:
    def maxProfit(self,prices,fee):
        n=len(prices)
        buy=-(prices[0]+fee)
        sell=0

        for i in range(1,n):
            buy=max(buy,sell-prices[i]-fee)
            sell=max(sell,buy+prices[i])

        return sell

prices = [1, 3, 2, 8, 4, 9]
fee = 2
"""
prices = [1,3,7,5,10,3]
fee = 3
"""
res=Solution().maxProfit(prices,fee)
print(res)