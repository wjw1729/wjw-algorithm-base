"""
author:wjw
分析：S,将上一个间距存在m中，这一个存在n中，比较n是否为m-1~m+1
official:时间复杂度O(n**2)
        如果第i个间隔>i，则不对，用来降低搜索复杂度
        
"""


class Solution:
    def canCross(self, stones):
        n = len(stones)
        dp = [[False for i in range(n)] for i in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False

        for i in range(1, n):
            for j in reversed(range(0, i)):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True
        return False


stones = [0, 1, 3, 5, 6, 8, 12, 17]
stones = [0, 1, 2, 3, 4, 8, 9, 11]

res = Solution().canCross(stones)
print(res)
