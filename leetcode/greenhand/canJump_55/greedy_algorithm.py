"""
author:wjw
分析：贪心算法.不用维护整个list，维护一个标量即可。
"""


class Solution:
    def canJump(self, nums):
        n = len(nums)
        rightmost = 0

        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])

            if rightmost >= n - 1:
                return True
        return False


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
res = Solution().canJump(nums)
print(res)
