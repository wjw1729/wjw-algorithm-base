"""
author:wjw
分析：由于要排序，时间复杂度最低为O(nlogn)。
"""

class Solution:
    def minSubArray(self, nums):
        sortedarray = nums[:]
        sortedarray.sort()
        n = len(nums)
        for left in range(n):
            if nums[left] != sortedarray[left]:
                break
        for right in range(n - 1, -1, -1):
            if nums[right] != sortedarray[right]:
                break

        return right - left + 1 if right>left else 0


nums=[2,6,4,8,10,9,15]
"""
nums=[1,2,3,4]
nums=[1]
"""
res=Solution().minSubArray(nums)
print(res)
