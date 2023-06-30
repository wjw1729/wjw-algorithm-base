"""
author:rank
分析：
"""

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:

        index_table = defaultdict(list)
        n = len(A)
        for i in range(n):
            index_table[A[i]].append(i)

        # 存每个数字的下标 有可能重复 因此list的元素可能不止一个

        dp = [[0] * n for i in range(n)]
        # dp[i][j] 以A[j] A[i]结尾的长度大于等于3的等差数列的个数
        res = 0
        for i in range(n):
            for j in range(i):
                # A[k], A[j], A[i]
                # 我们要找 A[i] - A[j] == A[j] - A[k]
                # 因此target为 2 * A[j] - A[i]
                target = 2 * A[j] - A[i]
                if target in index_table:
                    for k in index_table[target]:
                        if k < j:
                            dp[i][j] += (dp[j][k] + 1)

                res += dp[i][j]

        return res


nums = [2, 4, 6, 8, 10]
nums = [7, 7, 7, 7, 7]
res = Solution().numberOfArithmeticSlices(nums)
print(res)
