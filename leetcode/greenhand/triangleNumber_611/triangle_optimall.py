"""
authotr:others
分析：从右往左依次选三个数。
"""


class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)

        ans = 0
        for third in range(n - 1, 1, -1):
            left = 0
            right = third - 1
            while left < right:
                if nums[right] + nums[left] > nums[third]:
                    ans += right - left  ####从left到right-1，和right的组合都是符合要求的组合
                    right -= 1
                else:
                    left += 1  # left不符合就往右移
        return ans


nums = [2, 2, 3, 4]
res = Solution().triangleNumber(nums)
print(res)
