# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def amountOfTime(self, root, start: int) -> int:

        q = deque()
        q.append((root, 0))
        pa = {}

        while q:
            u, l = q.popleft()
            if u.val == start:
                dpth = l
                break

            if u.left:
                pa[u.left] = u
                q.append((u.left, l + 1))
            if u.right:
                pa[u.right] = u
                q.append((u.right, l + 1))

        q = deque()
        q.append((u, 0))
        t1 = 0

        vis=set()
        vis.add(u)

        while q:
            u, l = q.popleft()

            t1 = max(t1, l)


            if u.left and u.left not  in vis:
                q.append((u.left, l + 1))
                vis.add(u.left)
            if u.right and u.right not  in vis:
                q.append((u.right, l + 1))
                vis.add(u.right)
            if u in pa and pa[u] not in vis:
                q.append((pa[u],l+1))
                vis.add(pa[u])

        return t1




