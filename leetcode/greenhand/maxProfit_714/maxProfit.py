"""
author:wjw
分析：dp[i][0]表示i时刻买入能够获得的最大利润，dp[i][1]表示i时刻卖出能够获得的最大利润，dp[i][2]表示不动的最大利润(已买入),dp[i][3]表示不动的最大利润（已卖出）.
上面四个可以合并为两个，dp[i][0]表示i时刻已买入的最大利润（下一次为卖出操作），dp[i][1]表示已卖出的最大利润（下一次位买入操作）。
可以优化。
时间复杂度:O(n)
"""

class Solution:
    def maxProfit(self,prices,fee):
        n=len(prices)
        dp=[[float('-inf')]*2 for _ in range(n)]
        dp[0][0]=-(prices[0]+fee)
        dp[0][1]=0

        for i in range(1,n):

            dp[i][0]=max(dp[i][0],max(dp[i-1][0],dp[i-1][1]-prices[i]-fee))
            dp[i][1]=max(dp[i][1],max(dp[i-1][0]+prices[i],dp[i-1][1]))

        return dp[n-1][1]

prices = [1, 3, 2, 8, 4, 9]
fee = 2
prices = [1,3,7,5,10,3]
fee = 3
res=Solution().maxProfit(prices,fee)
print(res)
