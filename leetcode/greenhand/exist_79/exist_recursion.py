"""
author:wjw
分析：用递归来实现。
"""


class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        self.ans = False

        def bfs(point, path, getword):

            r, c = point
            path.add(point)
            getword += board[r][c]

            if getword == word:
                self.ans = True
                return
            if self.ans:
                return

            index = len(path)
            hasnextpoint = False
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in path and board[x][y] == word[index]:
                    hasnextpoint = True
                    bfs((x, y), path, getword)
                    path.pop()

            if not hasnextpoint:
                return

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    bfs((i, j), set(), '')

        return self.ans


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
#board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
#word = "SEE"
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
#board=[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
#word="AAAAAAAAAAAAABB"
res = Solution().exist(board, word)
print(res)
