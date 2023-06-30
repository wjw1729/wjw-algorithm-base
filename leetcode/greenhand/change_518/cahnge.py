"""
author:wjw
分析：
"""

class Solution:
    def change(self,amount,coins):
        n=len(coins)
        dp=[[0 for i in range(amount+1)]for i in range(n+1)]
        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(amount+1):
                m=j//coins[i-1]

                for k in range(m+1):
                    dp[i][j]+=dp[i-1][j-k*coins[i-1]]

                if i==1 and j==1:
                    print(1)

        return dp[n][amount]

amount=5
coins=[1,2,5]
res=Solution().change(amount,coins)
print(res)