"""
author:wjw
分析：递归不行。
    递推关系是从II衍生过来的。
"""


class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [[float('-inf')] * 4 for _ in range(n + 1)]

        dp[n] = [0, float('-inf'), float('-inf'), float('-inf')]
        for i in range(n - 1, -1, -1):
            for j in range(1, 4):
                if i + j <= n:
                    dp[i][j] = sum(stoneValue[i:i + j]) - max(dp[i + j])

        return max(dp[0])


values = [1, 2, 3, 7]
values = [1,2,3,-9]
values = [1,2,3,6]
values = [1,2,3,-1,-2,-3,7]
values = [-1,-2,-3]
res = Solution().stoneGameIII(values)
print(res)
