"""
author:wjw
分析：无穷乘式((((((k+1)k+1)k+1...)k+1=n，求最小k
    时间复杂度无限高
"""

class Solution:
    def smallestGoodBase(self,n):

        n=int(n)

        for k in range(2,n):
            total=0
            while total<n:
                total=total*k+1

            if total==n:
                return str(k)



n="1000000000000000000"
res=Solution().smallestGoodBase(n)
print(res)

