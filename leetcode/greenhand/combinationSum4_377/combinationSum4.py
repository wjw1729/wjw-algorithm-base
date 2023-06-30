"""
author:wjw
分析：先将数组排序为有序数组，用一个list保存所有<target的数的拆解总数
"""

from sortedcontainers import SortedList
class Solution:
    def combinationSum4(self,nums,target):
        nums=sorted(nums)
        SL=SortedList(nums)

        dp=[0]*(target+1)
        dp[0]=1

        for i in range(1,target+1):
            idx = SL.bisect_right(i)
            for j in range(idx):
                dp[i]+=dp[i-nums[j]]

        return dp[target]




nums=[9]
target=3
result=Solution().combinationSum4(nums,target)
print(result)

