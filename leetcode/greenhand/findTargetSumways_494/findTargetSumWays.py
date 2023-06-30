"""
author:wjw
分析:动态规划。dp[i][j]表示到i个nums时，和为j的不同表达式数目。i的范围0-len（nums）,j:[0,1000]U[-1000,0]
"""

class Solution:
    def findTargetSumWays(self,nums,target):
        n=len(nums)
        dp=[[0 for i in range(2001)]for i in range(n+1)]

        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(2001):
                if  -1000<=j-nums[i-1]<=1000 and -1000<=j+nums[i-1]<=1000:


                    dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j+nums[i-1]]
                    continue
                elif -1000<=j-nums[i-1]<=1000:
                    dp[i][j]=dp[i-1][j-nums[i-1]]
                    continue
                elif -1000<=j+nums[i-1]<=1000:
                    dp[i][j]=dp[i-1][j+nums[i-1]]
                    continue


        return dp[n][target]


nums=[1,1,1,1,1]
target=3
res=Solution().findTargetSumWays(nums,target)
print(res)


