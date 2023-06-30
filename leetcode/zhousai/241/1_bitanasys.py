"""
author:off
分析：按位进行分析。对所有元素中的某一位进行分析，第一种情况所有都为0，则所有异或和中该位都为0；第二种情况是至少有一个为1，则所有异或和中该位0和1的数量一样，都为2**(n-1)。
    时间复杂度：O(n)
"""


class Solution:
    def subsetXORSum(self, nums):
        n = len(nums)
        res = 0
        for num in nums:
            res |= num

        return res * 2 ** (n - 1)


nums = [1,3]
res = Solution().subsetXORSum(nums)
print(res)
