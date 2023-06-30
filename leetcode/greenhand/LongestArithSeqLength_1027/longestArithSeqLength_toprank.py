"""
author:rank
分析：
"""
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums):
        if len(nums) <= 1:
            return len(nums)
        memo = defaultdict(int)
        uniqNums = set()
        uniqNums.add(nums[0])
        for i in range(1, len(nums)):
            for num in uniqNums:
                pg = nums[i] - num
                if (num, pg) in memo:
                    memo[nums[i], pg] = memo[num, pg] + 1
                else:
                    memo[nums[i], pg] = 2
            uniqNums.add(nums[i])
        return max(memo.values())
