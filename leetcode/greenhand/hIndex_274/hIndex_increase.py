"""
author:wjw
分析：升序排列，判断依据不变，但是可以提前结束。因为在遍历过程中论文数量是递减的，所以第一个即为最大值。（降序则需遍历完）
"""

class Solution:
    def hIndex(self,citations):
        citations.sort()
        n=len(citations)

        for i in range(n):
            if citations[i]>=n-i:
                return n-i

        return 0


citations=[3,0,6,1,5]
res=Solution().hIndex(citations)
print(res)