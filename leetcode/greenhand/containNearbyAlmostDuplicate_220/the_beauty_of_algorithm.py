"""this is th beauty of algorithm.
"""

from sortedcontainers import SortedList
import bisect


class Solution:
    def containersNearbyAlmostDuplicate(self, nums, k, t):
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i]) #如果要改为bisect的话，需要-1,要不然如果插入在最右边，即最大值时，window[idx]out of range
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True

        return False


nums = [1, 2, 3, 1]
k = 1
t = 0
S = Solution()
result = S.containersNearbyAlmostDuplicate(nums, k, t)
print(result)
