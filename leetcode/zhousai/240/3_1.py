"""
author:wjw
分析：
"""

class Solution:
    def maxSumMinProduct(self, nums) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)

        left = [0] * n
        right = [n - 1] * n

        stack = []
        for i, num in enumerate(nums):
            while stack and num <= nums[stack[-1]]:
                right[stack[-1]] = i - 1
                stack.pop()

            if stack:
                left[i] = stack[-1] + 1
            stack.append(i)
        presum = [0]
        total = 0
        for num in nums:
            total += num
            presum.append(total)

        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * (presum[right[i] + 1] - presum[left[i]]))

        return ans % MOD

nums = [1,2,3,2]
res=Solution().maxSumMinProduct(nums)
print(res)