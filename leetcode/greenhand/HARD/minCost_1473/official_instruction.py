"""
author:wjw
分析：
设 dp(i,j,k) 表示将 [0,i] 的房子都涂上颜色，最末尾的第 i 个房子的颜色为 j+1，并且它属于第 k 个街区时，需要的最少花费。


"""


class Solution:
    def minCost(self, houses, cost, m: int, n, target: int) -> int:

        x = float('inf')
        dp = [[[x for i in range(target)] for i in range(n)] for i in range(m)]
        for j in range(n):
            if houses[0] == 0:
                dp[0][j][0] = cost[0][j]
                continue
            if houses[0] == j + 1:
                dp[0][j][0] = 0
                continue
            dp[0][j][0] = x

        for i in range(m):
            for j in range(n):
                for k in range(target):
                    for j0 in range(n):
                        if houses[i] != 0:
                            if houses[i] != j + 1:
                                dp[i][j][k] = x
                                print(1)
                            else:
                                if j0 == j:
                                    if i > 0:
                                        dp[i][j][k] = min(dp[i - 1][j0][k], dp[i][j][k])
                                else:
                                    if i > 0 and k > 0:
                                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1])
                        else:
                            if j0 == j:
                                if i > 0:
                                    dp[i][j][k] = min(dp[i - 1][j0][k] + cost[i][j], dp[i][j][k])
                            else:
                                if i > 0 and k > 0:
                                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1] + cost[i][j])

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        if ans == x:
            return -1

        return ans


house = [0, 0, 0, 0, 0]
house = [0, 2, 1, 2, 0]
cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
m = 5
n = 2
target = 3
res = Solution().minCost(house, cost, m, n, target)
print(res)
