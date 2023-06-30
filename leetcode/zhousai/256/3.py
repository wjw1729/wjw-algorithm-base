import bisect


# dp[i][j]表示将前i件物品装进限重为j的背包可以获得的最大价值
def select(nums, target):
    n = len(nums)
    dp = [[0] * (target + 1) for _ in range(n)]
    index = [[[]] * (target + 1) for _ in range(n)]

    for i in range(n):
        for j in range(target + 1):
            if j >= nums[i]:
                tmp = dp[i - 1][j - nums[i]] + nums[i]
                if tmp >=dp[i - 1][j]:
                    index[i][j] = index[i - 1][j - nums[i]][:] + [i]
                    dp[i][j] = tmp
                else:
                    dp[i][j] = dp[i - 1][j]
                    index[i][j] = index[i - 1][j][:]
            else:
                dp[i][j] = dp[i - 1][j]
                index[i][j] = index[i - 1][j][:]

    return index[n - 1][target]


class Solution:
    def minSessions(self, tasks, sessionTime: int) -> int:
        tasks.sort()

        n = len(tasks)
        need = 0

        while len(tasks) > 0:

            cur = tasks[-1]
            tasks.pop(-1)

            if tasks and sessionTime - cur >= tasks[0]:
                lista = select(tasks, sessionTime - cur)
                lista=list(set(lista))
                lista.sort()
                for i in lista[::-1]:
                    tasks.pop(i)
            need += 1

        return need


tasks = [1, 2, 3]
tasks = [1, 2, 3]
# tasks=[1,5,7,10,3,8,4,2,6,2]
sessionTime = 3
tasks = [2, 3, 3, 4, 4, 4, 5, 6, 7, 10]
#tasks=[1,2]
sessionTime = 12
tasks=[1,1,2,2,2,2,3,3,6,6,6,6]
sessionTime=10
tasks=[1,2,3,3,1,1,3,2,2,1]
sessionTime=11
res = Solution().minSessions(tasks, sessionTime)
print(res)
