"""
author:wjw
分析：降序排列，遍历，引用数量大于等于论文数量即可！
"""

class Solution:
    def hIndex(self,citations):
        citations.sort(reverse=True)
        n=len(citations)
        ans=0
        for i in range(n):
            if citations[i]>=i+1:
                ans=max(ans,i+1)

        return ans


citations=[3,0,6,1,5]
res=Solution().hIndex(citations)
print(res)
