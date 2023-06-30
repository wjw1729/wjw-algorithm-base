"""
author:wjw
分析：用两次二分法，第一次确定最大值位置，第二次确定重排后的list中是否有想要的元素。
"""


class Solution:
    def search(self, nums, target):
        n = len(nums)
        if nums[0]<nums[-1]:
            move=0

        left=0
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[left]:
                left=mid
            if nums[mid]<nums[right]:
                right=mid
            if right-left==1:
                move=right
                break

        nums = nums[move:] + nums[:move]

        left = 0
        right = n - 1
        if nums[0] == target:
            return move
        if nums[n-1] == target:
            return (n-1+move)%n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return (mid + move) % n
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
nums=[1,2,3,4,5,6,7]
nums=[3,5,1]
target=0
nums=[4,5,6,7,0,1,2]
target=6
res = Solution().search(nums, target)
print(res)
