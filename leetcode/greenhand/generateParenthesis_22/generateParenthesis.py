"""
author:wjw
分析：
    dfs如何从i->i+1。递推关系。在上一个结果上，加入”（“”）“。插空。
"""

import time
class Solution:
    def generateParenthesis(self, n: int):

        def dfs(ans):
            next = []
            p = len(ans)
            q = len(ans[0])
            for i in range(p):
                for j in range(q + 1):
                    s1 = ans[i][0:j] + "(" + ans[i][j:]
                    for k in range(j + 1, q + 2):
                        s2 = s1[0:k] + ")" + s1[k:]
                        next.append(s2)
            return list(set(next))

        ans = ['()']
        for i in range(n - 1):
            ans = dfs(ans)

        return ans


t1=time.time()
n = 8
res = Solution().generateParenthesis(n)
print(res)
print(len(res))
print(time.time()-t1)
