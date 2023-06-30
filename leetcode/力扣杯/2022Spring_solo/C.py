# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class segtree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.tag = 0
        self.total = 0
        self._left = self._right = None

    @property
    def mid(self):
        return self.start + (self.end - self.start) // 2

    @property
    def left(self):
        self._left = self._left or segtree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or segtree(self.mid + 1, self.end)
        return self._right

    def push(self):
        self.left.total = self.tag * (self.left.end - self.left.start + 1)
        self.right.total = self.tag * (self.right.end - self.right.start + 1)
        self.left.tag = self.tag
        self.right.tag = self.tag
        self.tag = 0

    def update(self, l, r, val):
        if l <= self.start and self.end <= r:
            self.total = val * (self.end - self.start + 1)
            self.tag = val
            return

        if self.tag != 0 and self.start != self.end:
            self.push()

        if l <= self.mid:
            self.left.update(l, r, val)
        if r > self.mid:
            self.right.update(l, r, val)

        self.total = self.left.total + self.right.total

    def query(self, l, r):
        if l <= self.start and self.end <= r:
            return self.total

        if self.tag != 0:
            self.push()

        res = 0
        if l <= self.mid:
            res += self.left.query(l, r)

        if r > self.mid:
            res += self.right.query(l, r)

        return res
from collections import deque
import bisect

class Solution:
    def getNumber(self, ls,  ops) -> int:

        ls.sort()

        red=[]

        for op,x,y in ops:
            if op==0:
                idx=bisect.bisect_right(x)

            else:
                if red==[]:
                    red.append(x)
                    red.append(y)





ls=[1,2,3,4,5]
ops = [[1,1,4],[1,1,3],[0,3,5]]
res=Solution().getNumber(ls,ops)
print(res)



