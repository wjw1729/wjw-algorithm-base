"""
author:wjw
分析：mask范围为[0,2**n-1]表示nums2中当前的选取状态，f[mask]表示在该选取状态下的最小异或和
"""


class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        x = float('inf')
        dp = [x] * (2 ** n)
        dp[0] = 0
        for mask in range(2 ** n):
            c = bin(mask).count('1')
            for i in range(n):
                dp[mask] = min(dp[mask], dp[mask ^ (2 ** i)] + (nums1[c - 1] ^ nums2[i]))

        return dp[2 ** n - 1]


nums1 = [1, 0, 3]
nums2 = [5, 3, 4]
res = Solution().minimumXORSum(nums1, nums2)
print(res)
