"""
author:wjw
分析：
"""

class Solution:
    def findKthLargest(self,nums,k):
        nums.sort(reverse=True)
        return nums[k-1]


nums=[3,2,1,5,6,4]
k=2
res=Solution().findKthLargest(nums,k)
print(res)