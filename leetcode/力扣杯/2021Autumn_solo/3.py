
class Solution:
    def flipChess(self, chessboard) -> int:

        n = len(chessboard)
        m = len(chessboard[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def flipnums(r, c):

            nonlocal board

            nxtturn = []
            for dire in directions:
                x = r + dire[0]
                y = c + dire[1]

                if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                    continue
                changelist = []
                changelist.append((x, y))
                check = False
                while board[x][y] == 'O':
                    x += dire[0]
                    y += dire[1]

                    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                        break

                    changelist.append((x, y))
                    if board[x][y] == '.':
                        break
                    if board[x][y] == 'X':
                        check = True
                        changelist.pop()
                        break

                if check:
                    for x, y in changelist:
                        board[x][y] = 'X'
                        nxtturn.append((x, y))

            ans = len(nxtturn)

            for x, y in nxtturn:
                ans += flipnums(x, y)

            return ans

        queue = []
        for i in range(n):
            for j in range(m):
                if chessboard[i][j] == 'O':
                    for dire in directions:
                        if 0 <= i + dire[0] < n and 0 <= j + dire[1] < m and chessboard[i + dire[0]][j + dire[1]]=='.':
                            queue.append((i + dire[0], j + dire[1]))

        res = 0

        for node in queue:
            board = [list(x) for x in chessboard]
            res = max(res, flipnums(node[0], node[1]))

        return res


chessboard = ["....X.", "....X.", "XOOO..", "......", "......"]
#chessboard = [".X.", ".O.", "XO."]
chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]
res = Solution().flipChess(chessboard)
print(res)
