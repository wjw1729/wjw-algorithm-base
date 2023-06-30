"""
author:wjw
分析：用递归来做.total函数返回每位玩家的最优选择。总体目标是先手玩家取数为正值，后手玩家取数为负值。
"""


class Solution:
    def predictTheWinner(self, nums):
        def total(start, end, turn):
            if start == end:
                return nums[start] * turn

            res1 = nums[start] * turn + total(start + 1, end, -turn)
            res2 = nums[end] * turn + total(start, end - 1, -turn)
            return max(res1 * turn, res2 * turn) * turn

        return total(0, len(nums) - 1, 1) >= 0


nums = [1, 5, 2]
nums = [1, 5, 233, 7]
res = Solution().predictTheWinner(nums)
print(res)
