"""
author:
分析：其实pow函数自带了取模的方法。
"""

class Solution:
    def countGoodNumbers(self,n):
        even=(n+1)//2
        odd=n//2

        return (pow(5,even,10**9+7)*pow(4,odd,10**9+7))%(10**9+7)




n=50000000000000000000000000
res=Solution().countGoodNumbers(n)
print(res)