"""
author:wjw
分析：回溯算法+剪枝。
这个是最好的方法。
"""
from collections import Counter
import time


class Solution:
    def exist(self, board, word):

        def trackback(i, j, k):

            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if trackback(x, y, k + 1):
                        result = True
                        break
            visited.remove((i, j))
            return result

        m = len(board)
        n = len(board[0])

        counter = Counter([x for l in board for x in l])
        wordcounter = Counter(word)

        for key in wordcounter:
            if wordcounter[key] > counter[key]:
                return False

        visited = set()
        for i in range(m):
            for j in range(n):
                if trackback(i, j, 0):
                    return True

        return False


t1 = time.time()
board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
word = "AAAAAAAAAAAAABB"
res = Solution().exist(board, word)
print(res)
print(time.time() - t1)
