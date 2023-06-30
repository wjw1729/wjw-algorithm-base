"""
属性名：类型=默认值

"""


class Trie:
    string: str = ''
    children: dict
    isaword: bool = False

    def __init__(self):
        self.children = dict()


class Solution:
    def findWords(self, board, words):

        root = Trie()

        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Trie()
                cur = cur.children[ch]

            cur.string = word
            cur.isaword = True

        m = len(board)
        n = len(board[0])
        vis = [[True] * n for _ in range(m)]
        ans = []

        def dfs(r, c, cur):
            if board[r][c] in cur.children:
                cur = cur.children[board[r][c]]
                if cur.isaword:
                    if cur.string not in ans:
                        ans.append(cur.string)

                vis[r][c] = False
                for x, y in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and vis[x][y]:
                        dfs(x, y, cur)

                vis[r][c] = True

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return ans


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
board = [["a","b"],["c","d"]]
words = ["abcb"]
board=[["a","a"]]
words=["aa"]
res = Solution().findWords(board, words)
print(res)
