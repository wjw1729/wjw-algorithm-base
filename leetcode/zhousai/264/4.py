from collections import defaultdict,deque
class Solution:
    def minimumTime(self, n: int, relations, time) -> int:

        indeg = [0] * (n + 1)

        towards = defaultdict(list)
        cost = [0] * (n + 1)

        for pre, nxt in relations:
            towards[pre].append(nxt)
            indeg[nxt] += 1

        queue = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                queue.append(i)
                cost[i] = time[i - 1]

        while queue:
            node = queue.popleft()

            for nxt in towards[node]:
                cost[nxt] = max(cost[nxt], cost[node] + time[nxt - 1])

                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)

        return max(cost[1:])



n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
res=Solution().minimumTime(n,relations,time)
print(res)