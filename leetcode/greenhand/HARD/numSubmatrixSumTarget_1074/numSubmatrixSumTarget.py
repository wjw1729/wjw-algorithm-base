"""
author:wjw
分析：矩形区域+前缀和+哈希表
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]

                d = {0: 1}
                sum = 0
                for k in range(n):
                    sum += total[k]
                    if sum - target in d.keys():
                        ans += d[sum - target]
                    if sum in d.keys():
                        d[sum] += 1
                    else:
                        d[sum] = 1

        return ans


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
# matrix=[[1,-1],[-1,1]]
target = 0
"""
target=0
matrix=[[904]]
"""

res = Solution().numSubmatrixSumTarget(matrix, target)
print(res)
