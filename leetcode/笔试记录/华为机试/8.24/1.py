n, m = [int(x) for x in input().strip().split()]
matrix = []
for i in range(n):
    tmp = [int(x) for x in input().strip().split()]
    matrix.append(tmp)


class Solution:
    def maxSubmatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        presum = [[0] for _ in range(n)]

        for i in range(n):
            total = 0
            for j in range(m):
                total += matrix[i][j]
                presum[i].append(total)

        ans = float('-inf')

        for k in range(m):
            for l in range(k + 1, m + 1):
                for i in range(n):
                    total = 0
                    for j in range(i, n):
                        total += presum[j][l] - presum[j][k]
                        ans = max(ans, total)

        return ans


res = Solution().maxSubmatrix(matrix)
print(res)
