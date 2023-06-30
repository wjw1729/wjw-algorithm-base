"""
author:wjw
分析：迭代模块
"""

import itertools
class Solution:
    def permutation(self,s):

        ans=list(set(itertools.permutations(list(s))))
        return [''.join(x) for x in ans]

s='abc'
res=Solution().permutation(s)
print(res)