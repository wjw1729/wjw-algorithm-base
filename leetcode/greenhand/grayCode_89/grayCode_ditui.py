"""
author:wjw
分析：G(n+1)=['0'+x for x in G(n)] +['1'+x for x in reversed(G(n))]
"""

class Solution:
    def grayCode(self,n):

        pre=['']
        for i in range(n):
           pre=['0'+x for x in pre]+['1'+x for x in reversed(pre)]


        return [int(x,base=2) for x in pre]

n=3
res=Solution().grayCode(n)
print(res)