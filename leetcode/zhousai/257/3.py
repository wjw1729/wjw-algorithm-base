"""
author:wjw
分析：dp[i]表示首次访问i到访问i+1之前经过的天数

"""


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit):
        n = len(nextVisit)
        dp = [2] * n

        for i in range(1, n):
            k = nextVisit[i]
            for j in range(k, i):
                dp[i] += dp[j]

        return sum(dp[:-1])

nums=[0,0]
nums=[0,0,2]
nextVisit = [0,1,2,0]
res=Solution().firstDayBeenInAllRooms(nums)
print(res)