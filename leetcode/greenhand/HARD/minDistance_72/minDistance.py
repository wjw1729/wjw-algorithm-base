"""
author:wjw
分析：dp[i][j]表示word1[:i]和word2[:j]的最小编辑次数.
    只要是从头开始，就可以看作二维的动态规划，不要想成四维的动态规划。
    和不相交的线1035（最长公共子序列），那道题有点类似。动态规划的思考模式一模一样，就是公式略有差别。
"""


class Solution:
    def minDistance(self, word1, word2):

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m+1):
            for j in range(n+1):

                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue

                if word2[j - 1] == word1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[m][n]


word1 = "horse"
word2 = "ros"
res = Solution().minDistance(word1, word2)
print(res)
