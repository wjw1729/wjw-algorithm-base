"""
author:wjw
fenxi:dp
"""


class Solution:
    def calculateMinimumHP(self,dungeon):
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[float('inf')]*n for _ in range(m)]
        dp[m-1][n-1]=1-dungeon[m-1][n-1]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                if i==m-1:
                    dp[i][j]=dp[i][j+1]-dungeon[i][j]
                elif j==n-1:
                    dp[i][j]=dp[i+1][j]-dungeon[i][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                if dp[i][j]<=0:
                    dp[i][j]=1

        return dp[0][0]

dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
res = Solution().calculateMinimumHP(dungeon)
print(res)




