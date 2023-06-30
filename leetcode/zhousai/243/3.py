"""
author:wjw
分析：将空闲的服务器用一个最小堆维护(w,idx)，将工作状态的服务器用另外一个最小堆维护（t,idx）。
时间复杂度：O((m+n)logm)
"""
import heapq


class Solution:
    def assignTasks(self, servers, tasks):

        busy = []

        idle = [(w, i) for i, w in enumerate(servers)]

        heapq.heapify(idle)

        ts = 0

        def release():
            while busy and busy[0][0] <= ts:
                _, idx = heapq.heappop(busy)
                heapq.heappush(idle, (servers[idx], idx))

        ans = []

        for i, t_cost in enumerate(tasks):
            ts = max(i, ts)

            release()
            if not idle:
                ts = busy[0][0]
                release()

            _, idx = heapq.heappop(idle)
            heapq.heappush(busy, (ts + t_cost, idx))
            ans.append(idx)

        return ans

servers = [3,3,2]
tasks = [1,2,3,2,1,2]

#servers = [5,1,4,3,2]
#tasks = [2,1,2,4,5,2,1]
res=Solution().assignTasks(servers,tasks)
print(res)