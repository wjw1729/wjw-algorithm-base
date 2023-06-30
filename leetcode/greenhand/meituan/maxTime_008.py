"""
author:wjw
分析：求取树上每个点到小美和小团的最短距离。如果一个点到小团比小美远（或相等），小团是一定会被追上的。所以最远距离点的选取是在那些距离小团比小美近的点中的最远点。时间复杂度:O(n)
"""

from collections import defaultdict, deque

n, x, y = [int(x) for x in input().strip().split()]
links = []
for i in range(n - 1):
    tmp = [int(x) for x in input().strip().split()]
    links.append(tmp)


# 离小美近的点，小团是不能去的
class Solution:
    def maxtime(self, links, x, y, n):

        meidis = [0] * (n + 1)
        tuandis = [0] * (n + 1)

        linkmap = defaultdict(list)
        for u, v in links:
            linkmap[u].append(v)
            linkmap[v].append(u)

        queue = deque()
        queue.append((x, 0))
        bin = {x}

        while queue:
            u, level = queue.popleft()

            for v in linkmap[u]:
                if v not in bin:
                    meidis[v] = level + 1
                    queue.append((v, level + 1))
                    bin.add(v)

        queue = deque()
        queue.append((y, 0))
        bin = {y}

        while queue:
            u, level = queue.popleft()

            for v in linkmap[u]:
                if v not in bin:
                    tuandis[v] = level + 1
                    queue.append((v, level + 1))
                    bin.add(v)
        ans = 0
        for i in range(1, n + 1):
            if tuandis[i] < meidis[i]:
                ans = max(ans, meidis[i])
        return ans


res = Solution().maxtime(links, x, y, n)
print(res)