"""
author:wjw
分析：前缀和,BF,O(n**2)，
"""


class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        presum = [0]
        sum = 0
        for i in range(n):
            sum += nums[i]
            presum.append(sum)

        for i in range(2, n + 1):
            for j in range(0, i - 1):
                if (presum[i] - presum[j]) % k == 0:
                    return True

        return False


nums = [23, 2, 4, 6, 7]
nums = [23, 2, 6, 4, 7]
nums=[2,4,3]
k = 6
res = Solution().checkSubarraySum(nums, k)
print(res)
