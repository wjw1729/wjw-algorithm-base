"""
author:wjw
分析：
"""
import itertools


class Solution:
    def subset(self, nums):
        ans = []
        n = len(nums)
        for i in range(n + 1):
            x = list(itertools.combinations(nums, i))
            y = [list(m) for m in x]
            ans += y

        return ans


nums = [1, 2, 3]
res = Solution().subset(nums)
print(res)
