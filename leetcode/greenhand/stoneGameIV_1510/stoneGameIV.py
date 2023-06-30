"""
author:wjw
分析：dp[i]表示剩下i个石子时Alice能否赢。
    这里可以分析下递推关系进行化简。超时
"""

class Solution:
    def winnerSquareGame(self,n):

        dp=[False]*(n+1)

        for i in range(1,n+1):
            for j in range(1,int(pow(i,0.5))+1):
                dp[i]=dp[i] | (not dp[i-j**2])

        return dp[n]

n=4
res=Solution().winnerSquareGame(n)
print(res)