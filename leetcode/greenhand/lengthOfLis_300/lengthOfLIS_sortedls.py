"""
author:wjw
分析：贪心+二分查找。d[i]存储长度为i增序列的最小尾部数字。
"""
import bisect


class Solution:
    def lengthOfLis(self, nums):

        n = len(nums)
        d = [-10001]

        for i in range(n):
            index = bisect.bisect_left(d, nums[i])
            if index < len(d):
                d[index] = min(d[index], nums[i])
            else:
                d.append(nums[i])

        return len(d) - 1


nums = [10, 9, 2, 5, 3, 7, 101, 18]
res = Solution().lengthOfLis(nums)
print(res)
