class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])

        wrd_len = len(word)
        wrd_counter = {}
        for s in word:
            wrd_counter.setdefault(s, 0)
            wrd_counter[s] += 1

        valid_char = set(word)

        counter = {}
        for row in board:
            for s in row:
                if s in valid_char:
                    counter.setdefault(s, 0)
                    counter[s] += 1

        for k, v in wrd_counter.items():
            counter.setdefault(k, 0)
            if counter[k] < wrd_counter[k]:
                return False

        status = [[True] * n for _ in range(m)]

        def dfs(r, c, wrd_index):

            if board[r][c] == word[wrd_index]:
                if wrd_index == wrd_len - 1:
                    return True
                status[r][c] = False
                ans = False
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and status[x][y] == True:
                        ans = ans or dfs(x, y, wrd_index + 1)
                status[r][c] = True
                return ans
            else:
                return False

        res = False
        for i in range(m):
            for j in range(n):
                res = res or dfs(i, j, 0)

        return res


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
res = Solution().exist(board, word)
print(res)
