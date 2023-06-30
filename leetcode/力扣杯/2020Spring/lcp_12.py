"""
author:wjw
分析：二分。设计二分的判断函数——>每天工作T时长下，能否在完成m天内完成任务。
时间复杂度:O(n).
"""


class Solution:
    def minTime(self, time, m: int) -> int:

        n = len(time)

        def canCompleteThePlan(T):
            ans = 0

            total = 0
            maxnum = 0
            for i in range(n):
                total += time[i]
                maxnum = max(maxnum, time[i])

                if total - maxnum > T:
                    total = time[i]
                    maxnum = time[i]
                    ans += 1
            ans += 1
            return ans <= m

        left = 0
        right = sum(time) // m

        ans = 0
        while left <= right:
            mid = (left + right + 1) // 2

            if canCompleteThePlan(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans


time = [1, 2, 3, 3]
m = 4
res = Solution().minTime(time, m)
print(res)
