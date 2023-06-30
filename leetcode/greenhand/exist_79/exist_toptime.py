"""
author:wjw
分析：目前时间最快的方法。
"""

from collections import Counter

import time
class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        checked = [[False] * n for _ in range(m)]
        counter = Counter([n for l in board for n in l])
        word_counter = Counter(word)
        for key in word_counter:
            if word_counter[key] > counter[key]:
                return False

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or checked[i][j] or board[i][j] != word[k]:
                return False
            checked[i][j] = True
            res = backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i,j - 1,k + 1)
            checked[i][j] = False
            return res

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


t1=time.time()
board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
word = "AAAAAAAAAAAAABB"
res = Solution().exist(board, word)
print(res)
print(time.time()-t1)
