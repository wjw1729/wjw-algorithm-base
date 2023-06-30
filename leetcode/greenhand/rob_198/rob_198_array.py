"""
author:wjw
分析：前向计算，用数组计算存储，不使用递归，内存不会过多的占用

"""


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        size = len(nums)
        dp = [0] * size
        if size == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]


l = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
     185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
s = Solution()
result = s.rob(l)
print(result)
