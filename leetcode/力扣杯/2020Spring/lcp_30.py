"""
author:wjw
分析：遍历。在遍历过程中用最小堆维护出现过的怪物扣血量，遇到前缀和小于0的方块，则把之前出现过的扣血最多的怪物移到最后。
时间复杂度：O（nlogn）
"""

import heapq


class Solution:
    def magicTower(self, nums):
        if sum(nums) < 0:
            return -1

        heap = []
        total = 0
        ans = 0
        for num in nums:
            if num < 0:
                heapq.heappush(heap, num)
            total += num
            if total < 0:
                total -= heapq.heappop(heap)
                ans += 1
        return ans


nums = [100, 100, 100, -250, -60, -140, -50, -50, 100, 150]
res = Solution().magicTower(nums)
print(res)
