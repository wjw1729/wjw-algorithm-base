"""
author:wjw
分析：没说从两端取。这个是从两端取的程序。
"""


class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)

        dpa = [[0] * n for _ in range(n)]
        dpb = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dpa[i][j] = aliceValues[i]
                    dpb[i][j] = bobValues[i]
                else:
                    dpa[i][j] = max(aliceValues[i] - dpb[i + 1][j], aliceValues[j] - dpb[i][j - 1])
                    dpb[i][j] = max(bobValues[i] - dpa[i + 1][j], bobValues[j] - dpa[i][j - 1])

        if dpa[0][n - 1] > 0:
            return 1
        elif dpa[0][n - 1] == 0:
            return 0
        else:
            return -1


aliceValues = [2, 9, 1, 1, 1, 3, 5, 8, 8, 6, 8, 6, 2, 4]
bobValues = [1, 9, 7, 8, 3, 4, 2, 7, 8, 10, 1, 7, 10, 4]
res = Solution().stoneGameVI(aliceValues, bobValues)
print(res)
