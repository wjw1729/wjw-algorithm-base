"""
author:wjw
分析：卡塔兰数。
"""

class Solution:
    def numTrees(self,n):
        c=1
        for i in range(n):
            c=2*(2*i+1)/(i+2)*c

        return c

n=12
res=Solution().numTrees(n)
print(res)