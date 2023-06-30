"""
author:wjw
分析：
"""

class Solution:
    def maxValue(self, n: str, x: int) -> str:

        if int(n)>=0:
            length=len(n)
            for i in range(length):
                if x>int(n[i]):
                    return n[:i]+str(x)+n[i:]
                if i==length-1:
                    return n+str(x)
        else:
            n=n.strip('-')
            length = len(n)
            for i in range(length):
                if x < int(n[i]):
                    return '-'+n[:i ] + str(x) + n[i:]
                if i==length-1:
                    return '-'+n+str(x)

n = "7873"
x = 7
res=Solution().maxValue(n,x)
print(res)