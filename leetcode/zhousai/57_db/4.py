"""
author:wjw
分析：创建一个字典key为[0,n-1]，value为后面比他高的最小的index。
"""

from collections import defaultdict
class Solution:
    def canSeePersonsCount(self, heights) :

        ans=[]
        n=len(heights)
        
        d=defaultdict(int)
        for i in range(n-1,0,-1):
            if heights[i]>heights[i-1]:
                d[i-1]=i
            else:
                index=d[i]
                while index!=0 and heights[index]<heights[i-1]:
                    index=d[index]
                d[i-1]=index

        for i in range(n):
            tmp=0
            maxheight=0
            j=i+1
            while j!=0 and j<n:
                if maxheight<heights[j]:
                    tmp+=1
                    maxheight=heights[j]
                if heights[j]>heights[i]:
                    break
                j=d[j]
            ans.append(tmp)

        return ans

heights = [10,6,8,5,11,9]

res=Solution().canSeePersonsCount(heights)
print(res)
