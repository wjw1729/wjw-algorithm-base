"""
author:wjw
分析：格式化输出+zip(*)
"""


class Solution:
    def totalHammingDistance(self, nums):
        str_nums = map('{:032b}'.format, nums)
        str_nums_bits = zip(*str_nums)
        sum = 0
        for b in str_nums_bits:
            sum += b.count('0') * b.count('1')
        return sum


nums = [4, 14, 2]
res = Solution().totalHammingDistance(nums)
print(res)
