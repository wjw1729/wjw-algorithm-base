"""
author:official
分析：
时间复杂度:o(n**2)
"""


class Solution:
    def triangleNumber(self, nums):
        nums.sort()

        n = len(nums)

        ans = 0
        for i in range(n - 1):

            k = i + 1
            for j in range(i + 1, n):

                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1

                ans += max(k - j - 1, 0)

        return ans


nums = [2, 2, 3, 4]
nums = [0, 0, 0]
res = Solution().triangleNumber(nums)
print(res)
