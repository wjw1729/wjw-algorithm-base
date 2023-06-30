"""
author:official
分析：dp[i+1][j]表示到cost[i]时，和为j的最大选取数。where记录在[i+1][j]选取过的数的路径，where[i+1][j]=j表示cost[i]未被选取，where[i+1][j]=j-c表示该数已被选取
"""


class Solution:
    def largestNumber(self, cost, target):

        dp = [[float('-inf')] * (target + 1) for i in range(10)]
        where = [[0] * (target + 1) for i in range(10)]
        dp[0][0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i][j-c]+1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c
        if dp[9][target] < 0:
            return '0'
        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]
        return ''.join(ans)


cost = [5, 6, 7, 3, 4, 6, 7, 4, 8]
target = 29
cost=[4,3,2,5,6,7,2,5,5]
target=9

res = Solution().largestNumber(cost, target)
print(res)
