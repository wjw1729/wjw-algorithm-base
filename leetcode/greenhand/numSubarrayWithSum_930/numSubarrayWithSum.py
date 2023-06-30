"""
author:wjw
分析：前缀和+哈希表（字典）
"""


class Solution:
    def numSubarrayWithSum(self, nums, target):
        n = len(nums)

        num_sum = 0
        d = {0: 1}
        ans = 0
        for i in range(n):
            num_sum += nums[i]
            if num_sum - target in d:
                ans += d[num_sum - target]
            d.setdefault(num_sum, 0)
            d[num_sum] += 1

        return ans


nums = [0, 1, 1, 0, 1]
target = 2
res = Solution().numSubarrayWithSum(nums, target)
print(res)
