class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])

        presum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + land[i - 1][j - 1]

        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 or (i > 0 and land[i - 1][j] == 1) or (j > 0 and land[i][j - 1] == 1):
                    continue
                find = False

                for p in range(m, i, -1):

                    for q in range(n, j, -1):
                        if presum[p][q] + presum[i][j] - presum[p][j] - presum[i][q] == (p - i) * (q - j):
                            ans.append([i, j, p - 1, q - 1])
                            find = True
                            break
                    if find:
                        break

        return ans
