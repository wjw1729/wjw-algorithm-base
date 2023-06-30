"""
author:wjw
分析：用两个单调队列分别维护最大值和最小值。
    用单调非增的双端队列维护最大值。
    用单调非减的双端队列维护最小值。
    时间复杂度：O（n）
"""

from collections import deque


class Solution:
    def longestSubarray(self, nums, limit):

        left = 0
        ans = 0
        queueMax = deque()
        queueMin = deque()

        for right in range(len(nums)):
            while queueMax and queueMax[-1] < nums[right]:
                queueMax.pop()

            queueMax.append(nums[right])

            while queueMin and queueMin[-1] > nums[right]:
                queueMin.pop()
            queueMin.append(nums[right])

            while queueMax[0] - queueMin[0] > limit:
                if nums[left] == queueMax[0]:
                    queueMax.popleft()

                if nums[left] == queueMin[0]:
                    queueMin.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans


nums = [8, 2, 4, 7]
limit = 4
nums = [10,1,2,4,7,2]
limit = 5
nums = [4,2,2,2,4,4,2,2]
limit = 0
res = Solution().longestSubarray(nums, limit)
print(res)
