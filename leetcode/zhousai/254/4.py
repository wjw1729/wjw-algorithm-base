"""

"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells) -> int:
        def canfindpath(r, c, path):
            nonlocal cancheck
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < row and 0 <= y < col and (x, y) not in path and board[x][y] == 0:
                    # if path == {(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1)}:
                    #    print(1)
                    if x == row - 1:
                        return True
                    path.add((x, y))
                    if canfindpath(x, y, path):
                        cancheck = True
                    path.remove((x, y))

            if cancheck:
                return True

            return False

        n = len(cells)
        left = 0
        right = n - 1

        while left < right:

            board = [[0] * col for _ in range(row)]
            firstrow = set()

            mid = (left + right) // 2
            if mid == left:
                mid = right

            for x, y in cells[:mid + 1]:
                board[x - 1][y - 1] = 1
                if x == 1:
                    firstrow.add(y - 1)

            # if i == 1:
            #    print(1)
            check = False
            for j in range(col):
                if j not in firstrow:
                    cancheck = False
                    if canfindpath(0, j, {(0, j)}):
                        check = True
                        break
            if check:
                left = mid
            else:
                right = mid - 1

        return left


row = 2
col = 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
row = 2
col = 2
cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
row = 3
col = 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]

row = 5
col = 2
cells = [[5, 1], [1, 2], [3, 1], [2, 2], [3, 2], [1, 1], [5, 2], [2, 1], [4, 2], [4, 1]]

row = 55
col = 2
cells = [[53, 1], [25, 1], [9, 2], [3, 1], [54, 1], [14, 2], [28, 1], [4, 1], [44, 1], [20, 2], [28, 2], [24, 2],
         [50, 1], [47, 2], [21, 1], [47, 1], [22, 2], [10, 1], [17, 1], [13, 1], [12, 1], [37, 2], [46, 2], [51, 1],
         [32, 1], [51, 2], [6, 2], [49, 2], [13, 2], [34, 1], [33, 1], [38, 2], [52, 2], [26, 2], [46, 1], [20, 1],
         [33, 2], [23, 2], [17, 2], [1, 2], [3, 2], [50, 2], [25, 2], [19, 1], [21, 2], [49, 1], [29, 1], [30, 2],
         [41, 1], [16, 1], [39, 2], [9, 1], [48, 2], [23, 1], [27, 1], [43, 1], [45, 1], [31, 1], [40, 1], [6, 1],
         [42, 1], [8, 2], [12, 2], [29, 2], [36, 2], [39, 1], [41, 2], [10, 2], [44, 2], [14, 1], [35, 1], [30, 1],
         [2, 2], [34, 2], [55, 1], [18, 1], [32, 2], [27, 2], [4, 2], [37, 1], [38, 1], [16, 2], [26, 1], [15, 2],
         [19, 2], [5, 1], [45, 2], [43, 2], [55, 2], [35, 2], [54, 2], [42, 2], [22, 1], [11, 1], [48, 1], [1, 1],
         [36, 1], [24, 1], [8, 1], [2, 1], [7, 1], [15, 1], [31, 2], [18, 2], [7, 2], [52, 1], [40, 2], [53, 2],
         [11, 2], [5, 2]]
res = Solution().latestDayToCross(row, col, cells)
print(res)
