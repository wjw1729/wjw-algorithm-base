"""

"""

class Solution:
    def countSpecialSubsequences(self, nums) -> int:

        n=len(nums)
        dp=[[0]*3 for _ in range(n)]
        if nums[0]==0:
            dp[0][0]=1

        hashmap={0:-1,1:-1,2:-1}

        for i in range(n):
            if nums[i]==0:
                j=hashmap[0]
                dp[i][0]=2*dp[j][0]+1
                hashmap[0]=i
            elif nums[i]==1:
                j0=hashmap[0]
                j1=hashmap[1]
                dp[i][1]=dp[j0][0]+2*dp[j1][1]
                hashmap[1]=i
            elif nums[i]==2:
                j1=hashmap[1]
                j2=hashmap[2]
                dp[i][2]=dp[j1][1]+2*dp[j2][2]
                hashmap[2]=i
                ans=dp[i][2]
        return ans

nums=[0,1,2,0,1,2]
nums=[0,0,2,1,2,0]
res=Solution().countSpecialSubsequences(nums)
print(res)
