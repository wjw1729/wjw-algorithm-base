"""
author:wjw
分析：如果是直接暴力的话。时间复杂度应该是O(n**2)。
    按照区间来找最小高度。
"""

class Solution:
    def largestRectangleArea(self,heights):
        n=len(heights)

        ans=0
        for i in range(n):
            minheight=heights[i]

            for j in range(i,n):
                minheight=min(minheight,heights[j])
                ans=max(ans,(j-i+1)*minheight)


        return ans

heights=[2,1,5,6,3,2]
res=Solution().largestRectangleArea(heights)
print(res)


