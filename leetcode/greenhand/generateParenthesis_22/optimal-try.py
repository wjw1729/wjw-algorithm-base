"""
official:
回溯算法就是牛
"""

import time
class Solution:
    def generateParenthesis(self, n: int) :
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()


        backtrack([], 0, 0)
        return ans

t1=time.time()
n=8
res=Solution().generateParenthesis(n)
print(res)
print(len(res))
print(time.time()-t1)