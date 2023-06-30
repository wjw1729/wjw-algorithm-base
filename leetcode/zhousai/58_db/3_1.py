"""
author:wjw
分析：
"""

class Solution:
    def minSpaceWastedKResizing(self,nums,k):
        n=len(nums)

        dp=[[float('inf')]*(k+2) for _ in range(n)]

        g=[[0]*n for _ in range(n)]

        for i in range(n):
            best=0
            for j in range(i,n):
                best=max(best,nums[j])
                g[i][j]=best*(j-i+1)

        for i in range(n):
            for j in range(1,k+2):
                for m in range(i+1):
                    dp[i][j]=min(dp[i][j],(0 if m==0 else dp[m-1][j-1])+g[m][i])

        return dp[n-1][k+1]-sum(nums)

nums = [10, 20]
k = 0

nums = [10,20,30]
k = 1

nums = [10, 20, 15, 30, 20]
k = 2

nums = [2, 48, 18, 16, 15, 9, 48, 7, 44, 48]
k = 1

res = Solution().minSpaceWastedKResizing(nums, k)
print(res)
