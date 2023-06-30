"""
author:wjw
分析：动态规划+优化。
时间复杂度：O（n）
空间复杂度:O(1)
"""

class Solution:
    def wiggleMaxLength(self,nums):
        n=len(nums)
        up=1
        down=1

        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up=max(up,down+1)
            elif nums[i]<nums[i-1]:
                down=max(down,up+1)

        return max(up,down)

nums = [1, 7, 4, 9, 2, 5]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
res = Solution().wiggleMaxLength(nums)
print(res)