"""
author；wjw
分析：最小堆.这个好像不太好，因为是整除就行，而不用是丑数和元素相乘
"""

import heapq


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        heap = [a, b, c]
        his = {a, b, c}
        heapq.heapify(heap)

        for i in range(n):
            next_ugly = heapq.heappop(heap)
            print(next_ugly)
            for prime in [a, b, c]:
                num = prime  next_ugly
                if num not in his:
                    his.add(num)
                    heapq.heappush(heap, num)

        return next_ugly
n=5
a=2
b=11
c=13
res=Solution().nthUglyNumber(n,a,b,c)
print(res)