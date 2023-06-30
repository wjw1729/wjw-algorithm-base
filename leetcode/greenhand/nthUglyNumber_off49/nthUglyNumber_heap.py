"""
author:wjw
分析：最小优先队列（最小堆）
"""

import heapq


class Solution:
    def nthUglyNumber(self, n):

        heap = [1]
        heapq.heapify(heap)
        his = {1}
        for i in range(n):
            next_ugly = heapq.heappop(heap)

            for prime in [2, 3, 5]:
                if next_ugly * prime not in his:
                    his.add(next_ugly * prime)
                    heapq.heappush(heap, next_ugly * prime)

        return next_ugly


n = 10
res = Solution().nthUglyNumber(n)
print(res)
