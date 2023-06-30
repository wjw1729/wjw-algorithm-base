"""
author:wjw
分析：
"""


class Solution:
    def maximumAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        n = len(arr)
        dp = [1] * n

        for i in range(1, n):
            if arr[i] == arr[i - 1] and arr[i] <= dp[i - 1]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp[-1]


arr = [1, 5, 5, 5, 5, 5, 5, 5]
res = Solution().maximumAfterDecrementingAndRearranging(arr)
print(res)
