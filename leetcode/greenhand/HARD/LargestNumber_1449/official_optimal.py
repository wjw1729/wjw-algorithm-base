"""
author:wjw
分析：
"""


class Solution:
    def largestNumber(self, cost, target):

        dp = [float('-inf')] * (target + 1)
        dp[0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j >= c and dp[j] <= dp[j - c] + 1:
                    dp[j] = dp[j - c] + 1

        if dp[target] == float('-inf'):
            return '0'

        cost.reverse()
        i = target
        ans = []

        while i > 0:
            for c in cost:
                if i >= c and dp[i - c] + 1 == dp[i]:
                    ans.append(str(9 - cost.index(c)))
                    i = i - c
                    break
        return ''.join(sorted(ans, reverse=True))


cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9
cost = [1000, 30, 105, 70, 42, 1000, 1000, 1000, 1000]
target = 503

res = Solution().largestNumber(cost, target)
print(res)
