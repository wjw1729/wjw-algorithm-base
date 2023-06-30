"""
author:wjw
分析：依据列表的长度奇偶分为两种情况，再比较当前情况下可行最大解的大小xxxxxxxxxxxxxxxxxxxxxx
"""


class Solution:
    def rob(self, nums) -> int:
        top=[]
        for i in range(1,len(nums)-2):
            if nums[i]>=nums[i-1]+nums[i+1]:
                top.append(nums[i])
                nums[i-1:i+2]=[0,0,0]
        if len(nums)==1:
            return nums[0]
        if len(nums) % 2 == 0:
            sum1 = sum(nums[::2])+sum(top)
            sum2 = sum(nums[1::2])+sum(top)
            return max(sum1, sum2)
        if len(nums) % 2 == 1:
            sum1 = sum(nums[::2])-nums[-1]+sum(top)
            sum2 = sum(nums[::2]) - nums[0]+sum(top)
            sum3 = sum(nums[1::2])+sum(top)
            return max(sum1, sum2, sum3)


l = [4,1,2,7,5,3,1]
#l=[1,2,3,1]
s = Solution()
res = s.rob(l)
print(res)
