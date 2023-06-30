"""
author:wjw
分析：迭代实现.O（n*2**n）
"""


class Solution:
    def subsetXORSum(self, nums):
        ans = 0
        n = len(nums)

        for i in range(2 ** n):
            tmp = 0
            for j in range(n):
                if i & 2 ** j:
                    tmp ^= nums[j]

            ans += tmp
        return ans


nums = [1, 2, 2]
res = Solution().subsetXORSum(nums)
print(res)
