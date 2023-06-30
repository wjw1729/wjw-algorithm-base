""""
"""


class Solution:
    def eraseOverlapIntervals(self,intervals):
        intervals.sort(key=lambda x:x[1])

        ans=1
        left=intervals[0][0]
        right=intervals[0][1]
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]>=right:
                ans+=1
                left=intervals[i][0]
                right=intervals[i][1]

        return n-ans

intervals=[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
res=Solution().eraseOverlapIntervals(intervals)
print(res)
