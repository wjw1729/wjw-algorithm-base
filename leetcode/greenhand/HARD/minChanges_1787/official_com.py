"""
author:wjw
分析：把所有的异或和表示一遍。
"""

from collections import Counter


class Solution:
    def minChanges(self, nums, k):
        n = len(nums)
        MAXX = 2 ** 10
        x = float('inf')
        f = [x] * MAXX
        f[0] = 0

        for i in range(k):

            counter = Counter()
            size = 0
            for j in range(i, n, k):
                counter[nums[j]] += 1
                size += 1

            t2min = min(f)

            g = [t2min] * MAXX

            for mask in range(MAXX):

                for x, countx in counter.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)

            f = [size + val for val in g]
        return f[0]


nums = [1, 2, 0, 3, 0]
k = 1
res = Solution().minChanges(nums, k)
print(res)
