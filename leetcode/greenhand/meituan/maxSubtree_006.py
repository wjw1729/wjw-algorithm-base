"""
author:wjw
分析：
"""
from collections import defaultdict

n, k = [int(x) for x in input().strip().split()]
link = []
for i in range(n - 1):
    tmp = [int(x) for x in input().strip().split()]
    link.append(tmp)
level = [int(x) for x in input().strip().split()]


class Solution:
    def maxSubtree(self,n, graph, level, k):
        MOD = 10 ** 9 + 7


        def Subtreenum(u, minnode, fa):
            res = 1
            for v in graph[u]:
                if v != fa and (level[minnode] + k >= level[v] > level[minnode] or (
                        level[v] == level[minnode] and v > minnode)):
                    res *= (Subtreenum(v, minnode, u) + 1)
                    res %= MOD
            return res

        ans = 0
        for i in range(1, n + 1):
            ans += Subtreenum(i, i, 0)
            print(ans)
            ans %= MOD
        return ans


graph = defaultdict(list)
for u, v in link:
    graph[u].append(v)
    graph[v].append(u)

level = [0] + level

res = Solution().maxSubtree(n,graph, level, k)
print(res)
