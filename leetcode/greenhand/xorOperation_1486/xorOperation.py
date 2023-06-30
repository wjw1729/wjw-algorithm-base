"""
author:wjw
分析:太简单了，不用分析
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans = ans ^ start
            start += 2
        return ans

n=5
start=0
res=Solution().xorOperation(n,start)
print(res)