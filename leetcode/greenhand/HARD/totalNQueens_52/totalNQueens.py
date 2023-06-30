"""
author:wjw
分析：N皇后
"""

class Solution:
    def totalNQueens(self,n):

        self.ans=0
        def backtrack(col,queen):

            if col==n:
                self.ans+=1
                return

            f_minus=set()
            f_add=set()
            for i in range(len(queen)):
                f_minus.add(i-queen[i])
                f_add.add(i+queen[i])

            for i in range(n):
                if i not in queen and col-i not in f_minus and col+i not in f_add:
                    queen.append(i)
                    backtrack(col+1,queen)

                    queen.pop()

        backtrack(0,[])
        return self.ans


n=1
res=Solution().totalNQueens(n)
print(res)
