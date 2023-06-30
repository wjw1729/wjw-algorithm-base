"""
author:wjw
分析：动态规划优化。
时间复杂度:O(m*n**2)
空间复杂度:O(n)
"""

from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)

        f = [float('inf')] * n

        indexmap = defaultdict(list)
        keyset = set(key)

        for i in range(n):
            if ring[i] in keyset:
                indexmap[ring[i]].append(i)

        for i in indexmap[key[0]]:
            f[i] = min(abs(i), n - abs(i)) + 1

        for ch in key[1:]:
            g = [float('inf')] * n
            for j in indexmap[ch]:
                for k in range(n):
                    g[j] = min(g[j], f[k] + min(abs(j - k), n - abs(j - k)) + 1)

            f = g
        return min(f)


ring = "godding"
key = "gd"
ring = "caotmcaataijjxi"
key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
res = Solution().findRotateSteps(ring, key)
print(res)
