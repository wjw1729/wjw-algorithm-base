"""
author:wjw
分析：
"""

class Solution:
    def findMaximumXOR(self, nums) :
        maxXor=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxXor=max(maxXor,nums[i]^nums[j])



        return maxXor



nums=[3,10,5,25,2,8]
res=Solution().findMaximumXOR(nums)
print(res)