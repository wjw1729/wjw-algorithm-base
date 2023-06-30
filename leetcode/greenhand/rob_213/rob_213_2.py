"""
author:wjw
分析：使用数组前向计算存储的方法来做,只用在size-1处使用dpp
"""


class Solutuion:
    def rob(self, nums):
        if not nums:
            return 0

        size = len(nums)
        dp = [0] * size  # dp[i]用来记录从0-num[i]的最大值
        dpp = [0] * size  # 用来记录从1-num[i]的最大值

        if size == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        dpp[0] = 0
        dpp[1] = nums[1]

        for i in range(2, size):
            if i == size - 1:
                dp[i] = max(dpp[i - 2] + nums[i], dp[i - 1])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            dpp[i] = max(dpp[i - 2] + nums[i], dpp[i - 1])

        print(dp, dpp)
        return dp[size - 1]


l = [1, 2, 3, 1]
s = Solutuion()
result = s.rob(l)
print(result)
