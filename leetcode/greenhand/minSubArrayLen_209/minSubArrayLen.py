"""
author:wjw
分析：前缀和+二分查找。O(nlogn)
"""
import bisect


class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        pre = [0]
        pre_sum = 0
        ans = float('inf')

        for i in range(n):
            pre_sum += nums[i]
            index = bisect.bisect(pre, pre_sum - target)
            if index != 0:
                ans = min(ans, len(nums) - index + 1)

            pre.append(pre_sum)

        return ans if ans!=float('inf') else 0


target = 7
nums = [2,3,1,2,4,3]
target=11
nums=[1,1,1,1,1,1]
res = Solution().minSubArrayLen(target, nums)
print(res)
