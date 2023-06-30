import heapq


class Solution:
    def getOrder(self, tasks):

        n = len(tasks)

        rest = [(et, idx) for idx, (et, pt) in enumerate(tasks)]
        taskheap = []

        heapq.heapify(rest)

        ans = []
        ts = 0
        for i in range(n):
            if i == 5:
                print(1)
            if not taskheap:
                ts = max(ts, rest[0][0])

            while rest and rest[0][0] <= ts:
                _, idx = heapq.heappop(rest)
                heapq.heappush(taskheap, (tasks[idx][1], idx))

            pt, idx = heapq.heappop(taskheap)
            ts += pt
            ans.append(idx)

        return ans


tasks = [[35, 36], [11, 7], [15, 47], [34, 2], [47, 19], [16, 14], [19, 8], [7, 34], [38, 15], [16, 18], [27, 22],
         [7, 15], [43, 2], [10, 5], [5, 4], [3, 11]]
res = Solution().getOrder(tasks)
print(res)
