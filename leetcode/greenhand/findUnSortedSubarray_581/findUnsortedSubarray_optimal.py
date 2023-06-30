"""
author:wjw
分析：哈希表。从前往后维护一个i及以前的最大值的哈希表。从后往前维护一个i及之后最小值的哈希表。
从后往前找无序数组的最右端index，从前往后找无序数组的最左端index。
"""


class Solution:
    def minSubarray(self, nums):

        n = len(nums)
        maxhash = {0: float('-inf')}
        minhash = {n - 1: float('inf')}

        for i in range(1, n):
            maxhash[i] = max(nums[i - 1], maxhash[i - 1])
        for i in range(n - 2, -1, -1):
            minhash[i] = min(nums[i + 1], minhash[i + 1])

        for left in range(n):
            if nums[left] > minhash[left]:
                break
        for right in range(n - 1, -1, -1):
            if nums[right] < maxhash[right]:
                break
        return right - left + 1 if right > left else 0


nums = [2, 5, 6, 4, 8, 10, 9, 15]
nums = [1, 3, 5, 4, 2]
nums=[1,2,3,4,5]
res = Solution().minSubarray(nums)
print(res)
