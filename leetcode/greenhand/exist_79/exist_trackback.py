"""
author:wjw
分析：回溯算法。
"""

class Solution:
    def exist(self,board,word):

        m = len(board)
        n = len(board[0])
        wordlen = len(word)
        visited = set()

        def backtrack(i, j, k):

            visited.add((i, j))
            if board[i][j] != word[k]:
                visited.remove((i, j))
                return False
            if k == wordlen - 1 and board[i][j] == word[k]:
                return True

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if backtrack(x, y, k + 1):
                        return True
                    elif (x,y) in visited:
                        visited.remove((x,y))

        for i in range(m):
            for j in range(n):
                res = backtrack(i, j, 0)
                visited=set()
                if res:
                    return res
        return False



board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board=[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word="AAAAAAAAAAAAABB"
#board=[["C","A","A"],["A","A","A"],["B","C","D"]]
#word="AAB"
res = Solution().exist(board, word)
print(res)