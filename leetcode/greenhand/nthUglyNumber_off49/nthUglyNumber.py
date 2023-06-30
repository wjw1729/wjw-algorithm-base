"""
author:wjw
分析：
"""
from sortedcontainers import SortedList
class Solution:
    def nthUglyNumber(self,n):
        res=[]
        search_ls=SortedList([1])
        his={1}
        while len(res)<n:
            next_ugly=search_ls.pop(0)
            res.append(next_ugly)
            for prime in [2,3,5]:
                if next_ugly*prime not in his:
                    his.add(next_ugly*prime)
                    search_ls.add(next_ugly*prime)

        return res[n-1]

n=10
res=Solution().nthUglyNumber(n)
print(res)

