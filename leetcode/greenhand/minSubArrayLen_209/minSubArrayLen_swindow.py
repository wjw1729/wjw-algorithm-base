"""
author:wjw
分析：滑动窗口，表面O(n)
"""


class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        start = 0
        end = 0
        sum = 0
        ans = float('inf')

        for i in range(n):
            sum += nums[i]
            end += 1

            while sum >= target:
                ans = min(ans, end - start)
                start += 1
                sum -= nums[start - 1]

        return ans if ans!=float('inf') else 0


target = 11
nums = [1,1,1,1,1,1,1]
res = Solution().minSubArrayLen(target, nums)
print(res)
