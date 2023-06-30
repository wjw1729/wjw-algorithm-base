

class Solution:
    def longestCommonSubpath(self,n,paths):


        def two_lcs(path1,path2):
            m=len(path1)
            n=len(path2)

            dp=[[0]*(n+1) for i in range(m+1)]

            for i in range(m+1):
                for j in range(n+1):
                    if i==0:
                        continue
                    if j==0:
                        continue

                    if path1[i-1]==path2[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])

            return dp[-1][-1]
