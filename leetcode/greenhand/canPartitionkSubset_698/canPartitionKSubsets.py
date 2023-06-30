"""
author:wjw
分析：回溯算法。
"""


class Solution:
    def canPartitionKSubsets(self, nums, k):
        sums = sum(nums)

        if sums % k != 0:
            return False
        target = sums // k

        nums.sort()
        if nums[-1]>target:
            return False
        ans = nums[:]

        def backtrack(nums, target):
            nonlocal find, ans
            if find:
                return
            if target == 0:
                ans = nums[:]
                find = True
                return

            for i in range(len(nums) - 1, -1, -1):
                if nums[i] <= target:
                    tmp = nums.pop(i)
                    backtrack(nums, target - tmp)
                    nums.insert(i, tmp)

        for i in range(k):
            find = False
            nums = ans[:]
            backtrack(nums, target)
            print(find)
            print(ans)
            if not find:
                return False

        return True


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
nums = [85, 35, 40, 64, 86, 45, 63, 16, 5364, 110, 5653, 97, 95]
k = 7
res = Solution().canPartitionKSubsets(nums, k)
print(res)
