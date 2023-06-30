"""
author:wjw
分析：dp[i][j]表示key[i]==rings[j]的最少移动次数。状态转移方程：dp[i][j]=min(dp[i-1][k]+min(abs(j-k),n-abs(j-k))+1) k∈[0,n)。
    输出即为min(dp[m-1])。
    用m*n的空间来节省时间。
    时间复杂度：O（m*n**2）
"""

from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        dp = [[float('inf')] * n for i in range(m)]

        keyset = set(key)
        indexmap = defaultdict(list)
        for i in range(n):
            if ring[i] in keyset:
                indexmap[ring[i]].append(i)

        for i in range(m):
            for j in indexmap[key[i]]:
                if i == 0:
                    dp[i][j] = min(abs(j), n - abs(j)) + 1
                else:
                    for k in range(n):
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1)

        return min(dp[m - 1])


ring = "godding"
key = "gd"
ring="caotmcaataijjxi"
key="oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
res = Solution().findRotateSteps(ring, key)
print(res)
