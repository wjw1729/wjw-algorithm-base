"""
official:动态规划
分析：维护一个list，dp用于保存当前长度的最大整除子集的长度，再依此进行list的生成。

"""

from sortedcontainers import SortedList
class Solution:
    def largestDivisibleSubset(self,nums):
        n=len(nums)
        nums=sorted(nums)

        dp=[1]*n

        maxSize=1
        maxVal=0

        # O(n**2)
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]%nums[j]==0:
                    dp[i]=max(dp[i],dp[j]+1)


            if dp[i]>maxSize:
                maxSize=dp[i]
                maxVal=nums[i]


        res=SortedList()
        if maxSize==1:
            res.add(nums[0])
            return res


        # O(n)
        for i in reversed(range(n)):
            if dp[i]==maxSize and maxVal%nums[i]==0:
                res.add(nums[i])
                maxSize-=1
                maxVal=nums[i]

        return res


nums = [2,4,7,8,9,12,16,20]
# nums=[1,2,3]
result = Solution().largestDivisibleSubset(nums)
print(result)