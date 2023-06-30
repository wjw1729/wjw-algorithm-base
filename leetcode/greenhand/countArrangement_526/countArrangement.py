"""
author:wjw
分析：回溯算法+预处理。
    时间复杂度：O(n!)
"""
from collections import defaultdict


class Solution:
    def countArrange(self, n):

        match = defaultdict(list)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        vis = set()
        ans = 0

        def backtrack(index):
            if index == n + 1:
                nonlocal ans
                ans += 1
                return

            for i in match[index]:
                if i not in vis:
                    vis.add(i)
                    backtrack(index + 1)
                    vis.discard(i)

        backtrack(1)
        return ans


n = 15
res = Solution().countArrange(n)
print(res)
