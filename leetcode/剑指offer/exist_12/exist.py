"""
author:wjw
分析：依据词频统计提前进行剪枝。然后是回溯，或者说是dfs？
"""
from collections import defaultdict


class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        wrd_len = len(word)
        wordset = set(word)
        wrd_counter = defaultdict(int)
        for s in word:
            wrd_counter[s] += 1

        counter = defaultdict(int)

        for row in board:
            for s in row:
                if s in wordset:
                    counter[s] += 1

        for k, v in wrd_counter.items():
            if counter[k] < wrd_counter[k]:
                return False

        status = [[True] * n for _ in range(m)]

        def dfs(r, c, wrd_index):

            if board[r][c] == word[wrd_index]:
                if wrd_index == wrd_len - 1:
                    return True
                status[r][c] = False
                tmp = False

                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and status[x][y] == True:
                        tmp = tmp or dfs(x, y, wrd_index + 1)
                status[r][c] = True
                return tmp
            else:
                return False

        ans = False
        for i in range(m):
            for j in range(n):
                ans = ans or dfs(i, j, 0)
        return ans


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
board = [["a", "b"], ["c", "d"]]
word = "abcd"
board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
res = Solution().exist(board, word)
print(res)
