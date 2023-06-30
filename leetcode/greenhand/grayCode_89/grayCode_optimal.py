"""
author:wjw
分析：直接递推int形的关系，而非先求取二进制字符型grayCode，再转为int型
"""

class Solution:
    def grayCode(self,n):
        g=[0]
        for i in range(n):
            prefix=2**i
            g=g+[prefix+x for x in reversed(g)]

        return g

n=3
res=Solution().grayCode(n)
print(res)