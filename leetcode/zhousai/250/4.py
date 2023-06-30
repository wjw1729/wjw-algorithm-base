"""
author:wjw
分析：字典树+离线处理+深度优先搜索。
时间复杂度:O(（m+n）*C),C=18
"""

from collections import defaultdict


class Trie:
    left: 'Trie' = None  # 表示0
    right: 'Trie' = None  # 表示1
    cnt: int = 0


class Solution:
    def maxGeneticDifference(self, parents, queries):

        MAXLENGTH = 17
        tree = defaultdict(list)
        for u, v in enumerate(parents):
            tree[v].append(u)

        store = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            store[node].append((i, val))

        n = len(queries)
        ans = [0] * n

        root = Trie()

        def insert(x):
            cur = root
            for i in range(MAXLENGTH, -1, -1):
                if x & (1 << i) :
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                cur.cnt += 1


        def query(x):
            cur = root
            res = 0

            for i in range(MAXLENGTH, -1, -1):

                if x & (1 << i):
                    if cur.left and cur.left.cnt:

                        res |= 1 << i
                        cur = cur.left
                    else:
                        cur = cur.right
                else:
                    if cur.right and cur.right.cnt:

                        res |= 1 << i
                        cur = cur.right
                    else:
                        cur = cur.left
            return res

        def erase(x):
            cur = root
            for i in range(MAXLENGTH, -1, -1):
                if x & (1 << i):
                    cur = cur.right
                else:
                    cur = cur.left
                cur.cnt -= 1

        def dfs(u):

            insert(u)


            for idx, val in store[u]:
                ans[idx] = query(val)
            for v in tree[u]:
                dfs(v)
            erase(u)

        dfs(tree[-1][0])

        return ans


parents = [-1, 0, 1, 1]
queries = [[0, 2], [3, 2], [2, 5]]
res = Solution().maxGeneticDifference(parents, queries)
print(res)
