"""
author:wjw
分析:循环+指针+剪枝
"""


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = []
        for first in range(n - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:  #nums[f]和后三项的和>target，说明后续无合格
                break
            if nums[first] + nums[-3] + nums[-2] + nums[-1] < target:                   #nums[f]和末尾三项和<target,说明nums[f]小了，进入下一个循环。
                continue

            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                    break
                if nums[first] + nums[second] + nums[-2] + nums[-1] < target:
                    continue
                for third in range(second + 1, n - 1):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    four = target - nums[first] - nums[second] - nums[third]
                    if four < nums[third + 1]:
                        break
                    if four > nums[-1]:
                        continue
                    if four in nums[third + 1:]:
                        ans.append([nums[first], nums[second], nums[third], four])

        return ans


nums = [1, 0, -1, 0, -2, 2]
# nums = [2, 2, 2, 2, 2]
target = 0
res = Solution().fourSum(nums, target)
print(res)
