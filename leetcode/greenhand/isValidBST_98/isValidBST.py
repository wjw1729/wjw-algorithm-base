"""
author:wjw
分析：递归实现。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def helper(node, l, r):
            if not node:
                return True
            if node.val <= l or node.val >= r:
                return False

            return helper(node.left, l, node.val) and helper(node.right, node.val, r)

        return helper(root, float('-inf'), float('inf'))


def list2TreeNode(lista):
    root = TreeNode(lista.pop(0))
    queue = [root]

    while lista:
        node = queue.pop(0)

        left_val = lista.pop(0)
        if left_val != 'null':
            node.left = TreeNode(left_val)
            queue.append(node.left)
        right_val = lista.pop(0)
        if right_val != 'null':
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


lista = [4, 1, 5, 'null', 'null', 3, 6]
lista = [2, 1, 3]
root = list2TreeNode(lista)
res = Solution().isValidBST(root)
print(res)
