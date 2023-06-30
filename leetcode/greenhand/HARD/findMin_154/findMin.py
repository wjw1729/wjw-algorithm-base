"""
author:wjw
分析：二分加缩进
"""
class Solution:
    def findMin(self,nums):
        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right-=1

        return nums[right]



nums=[1,3,5]
#nums=[2,2,2,0,1]
res=Solution().findMin(nums)
print(res)
