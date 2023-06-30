"""
author:wjw
分析：类似题：33、153
"""


class Solution:
    def search(self, nums, target: int) -> bool:

        while len(nums) > 1 and nums[0] == nums[-1]:
            if nums[0] == target:
                return True
            else:
                nums.pop(0)
                nums.pop()

        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            return nums[0] == target


        if nums[0] < nums[-1]:
            move = 0
        else:
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= nums[left]:
                    left = mid
                if nums[mid] <= nums[right]:
                    right = mid
                if right - left == 1:
                    move = right
                    break

        nums = nums[move:] + nums[:move]

        left = 0
        right = n - 1
        if nums[0] == target or nums[-1] == target:
            return True

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

        return False


nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
target = 2
nums=[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
target=13
res = Solution().search(nums, target)
print(res)
