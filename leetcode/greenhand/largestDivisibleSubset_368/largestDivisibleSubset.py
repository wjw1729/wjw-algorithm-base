"""
author:wjw
分析：方法不好
"""
from sortedcontainers import SortedList


class Solution:
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        ans = 0
        for i in reversed(range(len(nums))):


            nums_copy=nums[:i]
            begin=True

            while begin==True or len(total)>1:
                s = nums[i]
                total = SortedList([s])
                begin=False
                for j in reversed(range(len(nums_copy))):
                    if s != nums_copy[j] and s % nums_copy[j] == 0:
                        s = nums_copy[j]
                        total.add(s)

                if len(total) > ans:
                    res = total
                    ans = len(total)
                if len(total)>=2:
                   nums_copy.remove(total[-2])
        return list(res)


nums = [4,8,10,240]
nums=[1,2,3]
result = Solution().largestDivisibleSubset(nums)
print(result)
