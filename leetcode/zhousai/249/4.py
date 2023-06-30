"""
author:wjw
分析：
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees):

        roothash = {}
        leaves = set()

        for tree in trees:
            roothash[tree.val] = tree

            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)

        count = 0
        for k in roothash:
            if k not in leaves:
                root = roothash[k]
                count += 1

        if count != 1:
            return None

        roothash.pop(root.val)

        prev=float('-inf')
        def dfs(node):
            if not node:
                return True

            if node.left and node.left.val in roothash:
                node.left = roothash[node.left.val]
                roothash.pop(node.left.val)

            if node.right and node.right.val in roothash:
                node.right = roothash[node.right.val]
                roothash.pop(node.right.val)

            if not dfs(node.left):
                return False

            nonlocal prev

            if node.val <= prev:
                return False

            prev = node.val

            return dfs(node.right)

        if dfs(root) and not roothash:
            return root
        else:
            return None
