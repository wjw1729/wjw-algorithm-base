"""
author:wjw
分析：广度优先搜索.
时间复杂度:O(C*n)。C为queries中能搜索的点个数，N为图中边数。
"""

from collections import deque, defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        strset = set()

        for a, b in equations:
            strset.add(a)
            strset.add(b)

        adj = defaultdict(list)

        n = len(equations)
        for i in range(n):
            u, v = equations[i]
            value = values[i]

            adj[u].append((v, value))
            adj[v].append((u, 1 / value))

        ans = []

        for s, t in queries:
            if s not in strset or t not in strset:
                ans.append(-1)
                continue
            if s == t:
                ans.append(1)
                continue
            queue = deque()
            queue.append((s, 1))
            bin = set()
            bin.add(s)
            find = False

            while queue:
                u, value = queue.popleft()
                for v, w in adj[u]:
                    if v == t:
                        ans.append(value * w)
                        find = True
                        break
                    if v not in bin:
                        queue.append((v, value * w))
                        bin.add(v)
                if find:
                    break
            if not find:
                ans.append(-1)

        return ans


equations = [["a", "b"], ["b", "c"], ["a", "c"]]
values = [2.0, 3.0, 6.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
res = Solution().calcEquation(equations, values, queries)
print(res)
