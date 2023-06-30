"""
author:wjw
分析：递归。
    所有的递归都可以使用迭代来进行代替。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        def buidmytree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            root = TreeNode(preorder[preorder_left])

            index = hashmap[preorder[preorder_left]]
            size_lefttree = index - inorder_left

            root.left = buidmytree(preorder_left + 1, preorder_left + size_lefttree, inorder_left, index - 1)

            root.right = buidmytree(preorder_left + size_lefttree + 1, preorder_right, index + 1, inorder_right)

            return root

        n = len(preorder)
        hashmap = {element: i for i, element in enumerate(inorder)}
        root = buidmytree(0, n - 1, 0, n - 1)

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = Solution().buildTree(preorder, inorder)
print(res)
