"""
author:wjw
分析：太简单了，没啥好分析的
"""

class Solution:
    def removeElement(self,nums,val):
        while val in nums:
            nums.remove(val)

        length=len(nums)
        return length


nums=[3,2,2,3]
val=3
S=Solution()
res=S.removeElement(nums,val)
print(res)