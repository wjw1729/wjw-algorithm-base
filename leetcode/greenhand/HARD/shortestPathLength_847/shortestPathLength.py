"""
auhtor:wjw
分析：会有重复访问一个节点，所以mask的求和，应该用或。
"""

import time
class Solution:
    def shortestPathLength(self, graph):

        n = len(graph)
        queue = []
        bin = set()
        mask = 1
        for i in range(n):
            queue.append((i, mask, 0))
            bin.add((i, mask))
            mask <<= 1

        while queue:
            node, mask, length = queue.pop(0)

            if mask == 2 ** n - 1:
                return length

            for next in graph[node]:
                tmp_mask = mask | (1 << next)
                if (next, mask) not in bin:
                    bin.add((next, tmp_mask))
                    queue.append((next, tmp_mask, length + 1))


t1=time.time()
graph = [[1, 2, 3], [0], [0], [0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
graph=[[1],[0,2,4],[1,3],[2],[1,5],[4]]
graph=[[1,2,3,4,5,6,7,8,9,10,11],[0,2,5,6,8],[0,1,4,5,6,9,10,11],[0,4,5,6,8,9,10,11],[0,2,3,5,6,8,10],[0,1,2,3,4,6,8,9,10,11],[0,1,2,3,4,5,8,10,11],[0,8],[0,1,3,4,5,6,7,9,10,11],[0,2,3,5,8,10],[0,2,3,4,5,6,8,9],[0,2,3,5,6,8]]
res = Solution().shortestPathLength(graph)
print(res)
print(time.time()-t1)