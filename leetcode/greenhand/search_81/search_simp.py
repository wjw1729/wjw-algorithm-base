"""
author:wjw
分析：直接用二分法确定，最小数所在位置！(即move次数)，然后再重排+二分法判断.
        这个好像不太行，因为针对[1,1,1,1,1,1,2,1,1,1,1,1,1]这类情况，返回的最小数位置，只是0，而不是2后面1的下标。
"""

class Solution:
    def search(self,nums,target):
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

        move=right

        nums=nums[move:]+nums[:move]

        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return True

        return False

nums = [2,5,6,0,0,1,2]
nums=[1]
nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
res=Solution().search(nums,target)
print(res)