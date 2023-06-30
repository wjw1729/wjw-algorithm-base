import bisect


class Solution:
    def minSessions(self, tasks, sessionTime: int) -> int:
        tasks.sort()

        n = len(tasks)
        need = 0

        while len(tasks) > 0:
            cur = tasks[-1]
            tasks.pop(-1)

            while tasks and sessionTime - cur >= tasks[0]:
                index = bisect.bisect(tasks, sessionTime - cur)
                cur += tasks.pop(index - 1)
            need += 1

        return need
