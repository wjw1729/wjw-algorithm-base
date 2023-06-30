"""
author:wjw
分析：递归.O(2**n)
"""


class Solution:
    def subXORSum(self, nums):
        ans = 0
        n = len(nums)

        def dfs(val, idx):
            nonlocal ans
            if idx == n:
                ans += val
                return

            dfs(val ^ nums[idx], idx + 1)
            dfs(val, idx + 1)

        dfs(0, 0)
        return ans


nums = [1, 2, 2]
res = Solution().subXORSum(nums)
print(res)
