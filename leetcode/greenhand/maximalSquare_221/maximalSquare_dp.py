"""
author:wjw
分析：动态规划。dp[i][j]表示以i,j为右下角所包含的最大正方形边数。
"""

class Solution:
    def maximalSquare(self,matrix):
        m=len(matrix)
        n=len(matrix[0])

        dp=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]!='0':
                    if i==0:
                        dp[i][j]=1
                        continue
                    if j==0:
                        dp[i][j]=1
                        continue
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

        return max([x for l in dp for x in l])**2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
#matrix = [["0","1"],["1","0"]]
res = Solution().maximalSquare(matrix)
print(res)