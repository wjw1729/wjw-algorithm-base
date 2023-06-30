"""
author:wjw
分析：基本功,,,,,,,,,
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def midfirst(tree):
    res = [tree.val]
    if tree.left != None:
        res = midfirst(tree.left) + res
    if tree.right != None:
        res = res + midfirst(tree.right)
    return res


class Solution:
    def increasingBST(self, root):
        l1 = midfirst(root)

        rootnode = TreeNode(l1[0])
        node = rootnode
        index = 1
        while index < len(l1):
            # node.left = None
            node.right = TreeNode(l1[index])
            node = node.right
            index = index + 1
        return rootnode


def list2TreeNode(l1):
    root = TreeNode(l1[0])
    nodequeue = [root]
    front = 0
    index = 1
    while index < len(l1):
        node = nodequeue[front]
        front = front + 1

        if l1[index] != 'null':
            node.left = TreeNode(l1[index])
            nodequeue.append(node.left)
        index = index + 1

        if index >= len(l1):
            break

        if l1[index] != 'null':
            node.right = TreeNode(l1[index])
            nodequeue.append(node.right)
        index = index + 1

    return root


if __name__ == '__main__':
    root = [5, 3, 6, 2, 4, 'null', 8, 1, 'null', 'null', 'null', 7, 9]
    tree = list2TreeNode(root)

    res = Solution().increasingBST(tree)
    print(1)
