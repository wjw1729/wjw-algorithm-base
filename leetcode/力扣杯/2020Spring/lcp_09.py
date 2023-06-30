"""
author:wjw
分析：贪心？。

"""


class Solution:
    def minJump(self, jump):
        n = len(jump)
        f = [float('inf')] * n
        f[0] = 0
        res = float('inf')

        max_dis = [0] * (n + 1)
        min_step = 0

        for i in range(n):
            if i > max_dis[min_step]:
                min_step += 1

            f[i] = min(f[i], min_step + 1)

            tmp = i + jump[i]
            if tmp >= n:
                res = min(res, f[i] + 1)
                return res
            else:
                f[tmp] = min(f[tmp], f[i] + 1)
                max_dis[f[i] + 1] = max(max_dis[f[i] + 1], tmp)
        return res


jump = [2, 5, 1, 1, 1, 1]
res = Solution().minJump(jump)
print(res)
