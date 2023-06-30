"""
author:wjw
分析：将jobs中的数尽可能平均的分配到k组中，
    回溯+剪枝+二分查找
"""


class Solution:
    def minimumTimeRequired(self, jobs, k: int) -> int:

        def check(limit):
            workloads = [0] * k
            jobs.sort(reverse=True)

            if backtrack(jobs, workloads, 0, limit):
                return True
            else:
                return False

        def backtrack(jobs, workloads, i, limit):
            if i >= len(jobs):
                return True

            cur = jobs[i]
            for j in range(len(workloads)):
                if workloads[j] + cur <= limit:
                    workloads[j] += cur

                    if backtrack(jobs, workloads, i + 1, limit):
                        return True

                    workloads[j] -= cur

                    if workloads[j] == 0:
                        break
            return False

        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l


jobs = [1, 2, 1, 1, 3, 4, 5, 6]
k = 3
jobs = [3, 2, 3]
k = 3
jobs = [1, 2, 4, 7, 8]
k = 2
res = Solution().minimumTimeRequired(jobs, k)
print(res)
