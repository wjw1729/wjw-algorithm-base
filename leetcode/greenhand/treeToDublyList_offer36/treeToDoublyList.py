"""
author:wjw
分析：将节点存储到list中，然后建立链接关系。
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):

        def inorder(root):
            if not root:
                return []
            else:
                return inorder(root.left) + root + inorder(root.right)

        nodels = inorder(root)
        n = len(nodels)
        for i in range(n):
            nodels[i].left = nodels[(i - 1) % n]
            nodels[i].right = nodels[(i + 1) % n]

        return nodels[0] if nodels != [] else None
