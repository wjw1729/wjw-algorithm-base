"""
author:wjw
分析：广度优先搜索。
"""


class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        queue = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:

                    bin = {(i, j)}
                    queue.append((i, j, 0, bin))
                    while queue:
                        r, c, index, bin = queue.pop(0)

                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= x < m and 0 <= y < n and (x, y) not in bin and board[x][y] == word[index + 1]:
                                if index + 1 == len(word) - 1:
                                    return True
                                bin.add((x, y))
                                queue.append((x, y, index + 1, bin.copy()))
                                bin.remove((x, y))

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "SEE"
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
# board = [["a", "a"]]
# word = "aaa"
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
board=[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word="AAAAAAAAAAAAAAB"

res = Solution().exist(board, word)
print(res)
