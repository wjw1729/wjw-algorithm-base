n = int(input().strip())
tasks = []
for i in range(n):
    tmp = [int(x) for x in input().strip().split()]
    tasks.append(tmp)

from collections import defaultdict


class Solution:
    def minTime(self, tasks):

        n = len(tasks)
        cost = []
        dependhash = defaultdict(list)
        for i in range(len(tasks)):
            t = tasks[i][-1]
            cost.append(t)
            for j in tasks[i][:-1]:
                dependhash[i].append(j)
                if i in dependhash[j]:
                    return -1

        extime = [float('inf')] * n

        def execute(i):
            if extime[i] != float('inf'):
                return

            if dependhash[i] == [-1]:
                extime[i] = cost[i]
            else:
                tmp = 0
                for j in dependhash[i]:
                    if extime[j] == float('inf'):
                        execute(j)
                    tmp = max(extime[j] + cost[i], tmp)

                extime[i] = tmp

            return

        for i in range(n):
            execute(i)

        return max(extime)


res = Solution().minTime(tasks)
print(res)
