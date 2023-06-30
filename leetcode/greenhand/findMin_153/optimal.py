"""
author:wjw
分析：遍历？
"""

class Solution:
    def findMin(self,nums):

        if nums[0]<=nums[-1]:
            return nums[0]
        n=len(nums)
        for i in range(n):
            if nums[i+1]<nums[i]:
                return nums[i+1]


nums=[3,4,5,1,2]
res=Solution().findMin(nums)
print(res)