"""
author:wjw
分析：动态规划+优化
"""


class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        pre = [int(x) for x in matrix[0]]
        ans = max(pre)

        for i in range(1, m):
            now = [0] * n
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        now[j] = 1
                        ans = max(ans, now[j])
                        continue
                    now[j] = min(pre[j - 1], pre[j], now[j - 1]) + 1
                    ans = max(ans, now[j])
            pre = now
        return ans ** 2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
#matrix = [["0", "1"], ["1", "0"]]
res = Solution().maximalSquare(matrix)
print(res)
