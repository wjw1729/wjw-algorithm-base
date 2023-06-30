import heapq
import math


class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        heap = []

        for i, pile in enumerate(piles):
            heapq.heappush(heap, (-pile, i))

        for i in range(k):
            pile, index = heapq.heappop(heap)
            piles[index] = math.ceil(piles[index] / 2)
            heapq.heappush(heap, (-piles[index], index))

        return sum(piles)


piles = [5, 4, 9]
k = 2
piles = [4, 3, 6, 7]
k = 3
res = Solution().minStoneSum(piles, k)
print(res)
