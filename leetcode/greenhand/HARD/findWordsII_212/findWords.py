"""
author：wjw
分析：找字符串和单词搜索I，没什么区别。只是这里搜索的单词对象从1变为了多个。所以初步构想是建立字典树。
"""


class Trie:
    string: str = ""
    children: dict
    isaword: bool = False

    def __init__(self):
        self.children = dict()


class Solution:
    def findWords(self, board, words):

        root = Trie()

        for word in words:
            cur = root
            for i in range(len(word)):
                if word[i] not in cur.children:
                    cur.children[word[i]] = Trie()
                    cur.children[word[i]].string = cur.string + word[i]

                cur = cur.children[word[i]]
                if i == len(word) - 1:
                    cur.isaword = True

        m = len(board)
        n = len(board[0])

        status = [[True] * n for _ in range(m)]
        ans = []

        def dfs(r, c, cur):

            if board[r][c] in cur.children:

                if cur.children[board[r][c]].isaword:
                    if cur.children[board[r][c]].string not in ans:
                        ans.append(cur.children[board[r][c]].string)

                status[r][c] = False
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and status[x][y] == True:
                        dfs(x, y, cur.children[board[r][c]])
                status[r][c] = True

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return ans


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
board=[["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words=["oa","oaa"]
res = Solution().findWords(board, words)
print(res)
