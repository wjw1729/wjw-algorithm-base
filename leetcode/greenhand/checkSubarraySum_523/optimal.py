"""
author:wjw
分析：取模+前缀和+哈希表
"""


class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)

        pre = nums[0]
        pre_set = set()

        for i in range(1, n):

            pre = (pre + nums[i]) % k
            if i==1:
                pre_sum_minus_2 = 0
            else:
                pre_sum_minus_2 = (pre_sum_minus_2 + nums[i - 2]) % k
            pre_set.add(pre_sum_minus_2)

            if pre in pre_set:
                return True

        return False



nums = [23, 2, 4, 6, 7]
nums = [23, 2, 6, 4, 7]
#nums=[2,4,3]
#nums=[0,0]
k = 13
res = Solution().checkSubarraySum(nums, k)
print(res)