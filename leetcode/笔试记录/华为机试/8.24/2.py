"""测试按例没拍全，现在按照是人踏上那块方框，如果剩余时间为0是不符合要求来算的。第三题在做。"""
from collections import deque

m,n=[int(x) for x in input().strip().split()]
matrix=[]
for i in range(m):
    tmp=[int(x) for x in input().strip().split()]
    matrix.append(tmp)


class Solution:
    def minTime(self, matrix):
        m, n = len(matrix), len(matrix[0])

        queue = deque()
        queue.append((0, 0, 0))

        bin = {(0, 0)}
        ans = float('inf')

        while queue:
            r, c, t = queue.popleft()

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in bin:
                    if x == m - 1 and y == n - 1 and t + 1 < matrix[x][y]:
                        ans = t + 1
                        break

                    if t + 1 < matrix[x][y]:
                        queue.append((x, y, t + 1))
                        bin.add((x, y))
        return ans if ans != float('inf') else -1

res=Solution().minTime(matrix)
print(res)

""""
matrix = [[3, 5, 4, 2, 3], [4, 5, 3, 4, 3], [4, 3, 5, 3, 2], [2, 5, 3, 3, 5], [5, 3, 4, 4, 3]]
res = Solution().minTime(matrix)
print(res)

"""
