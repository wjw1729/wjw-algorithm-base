"""
author:wjw
分析：这里必须要用nums[:]=才行，nums=不行，前者表示nums值的替换，后者表示开辟新空间赋值。
"""
from collections import Counter


class Solution:
    def sortColors(self, nums):
        d = Counter(nums)
        nums[:] = [0] * d[0] + [1] * d[1] + [2] * d[2]


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
