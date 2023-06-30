"""
author:wjw
分析：优先队列.O(nlogn).堆中加入索引，用于删除元素。将前面思路中的sortedlist换为优先队列，这样添加和删除的速度都会更快。
"""

import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)

        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = Solution().maxSlidingWindow(nums, k)
print(res)
