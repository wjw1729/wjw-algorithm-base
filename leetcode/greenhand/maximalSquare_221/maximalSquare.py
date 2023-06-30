"""
author:wjw
分析：强行遍历！
"""


class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    maxsquarerange = min(m - i - 1, n - j - 1)

                    earlystop = False
                    k = 0
                    for k in range(1, maxsquarerange+1):
                        for row in range(i, i + k + 1):
                            if matrix[row][j:j + k + 1] != ['1'] * (k + 1):
                                earlystop = True
                                break
                        if earlystop:
                            break
                    if earlystop:
                        ans = max(ans, k)
                        if ans==3:
                            print(1)
                    else:
                        ans = max(ans, k + 1)
                        if ans==3:
                            print(1)

        return ans ** 2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# matrix = [["0","1"],["1","0"]]
res = Solution().maximalSquare(matrix)
print(res)
