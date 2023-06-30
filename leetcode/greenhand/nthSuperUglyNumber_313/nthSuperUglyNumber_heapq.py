"""
author:wjw
分析：最小堆实现。
"""

import heapq
class Solution:
    def nthSuperUglyNumber(self,n,primes):
        heap=[]
        heapq.heappush(heap,1)
        his={1}

        for i in range(n):
            next_ugly=heapq.heappop(heap)
            for prime in primes:
                num=next_ugly*prime
                if num not in his:
                    his.add(num)
                    heapq.heappush(heap,num)

        return next_ugly

n=12
primes=[2, 7, 13, 19]
res=Solution().nthSuperUglyNumber(n,primes)
print(res)
