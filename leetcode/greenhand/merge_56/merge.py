"""
author:wjw
分析：先将区间按照左坐标值排序，左右坐标，分开存储。index_left保存每个要开始合并区间的左坐标索引，max_right表示区间的右坐标值。
"""

import bisect


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        interval_left = [x[0] for x in intervals]
        interval_right = [x[1] for x in intervals]

        ans = []
        index_left = 0
        max_right = interval_right[index_left]
        while index_left < n:
            temp = bisect.bisect(interval_left, max_right)
            max_right = max(interval_right[index_left:temp])
            if temp == n or max_right < interval_left[temp]:
                ans.append([interval_left[index_left], max_right])
                index_left = temp
                if temp != n:
                    max_right = interval_right[index_left]

        return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
intervals = [[1, 4], [2, 3]]
res = Solution().merge(intervals)
print(res)
