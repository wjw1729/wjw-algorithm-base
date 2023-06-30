"""
author:wjw
分析：动态规划。
时间复杂度:O(n)
空间复杂度:O(n)
"""


class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        up = [1] * n
        down = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(down[i - 1], up[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])


nums = [1, 7, 4, 9, 2, 5]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
res = Solution().wiggleMaxLength(nums)
print(res)
