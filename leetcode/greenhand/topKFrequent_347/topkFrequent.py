"""
author:wjw
分析：和692一样
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        d = Counter(nums)
        d1 = {}
        for key, val in d.items():
            if val in d1:
                d1[val].append(key)
            else:
                d1[val] = [key]

        ans = []
        while len(ans) < k:
            max_val = max(d1.keys())
            ans += d1[max_val]
            d1.pop(max_val)

        return ans


nums = [1, 1, 1, 2, 2, 3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)
