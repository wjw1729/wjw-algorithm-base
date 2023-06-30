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
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def dnode(root):
            if not root:
                return 0

            l = dnode(root.left)
            r = dnode(root.right)

            self.ans = max(self.ans, l + r + root.val)  # 选择当前结点为子树根节点的情况下，所能求得的最大路径和的值

            res = max(l, r) + root.val
            return res if res > 0 else 0      #大于0表示选择其中的左子树或右子树部分路径，=0表示不选该节点。

        dnode(root)
        return self.ans


def list2TreeNode(lista):
    root = TreeNode(lista.pop(0))
    queue = [root]

    while lista:
        node = queue.pop(0)
        left = lista.pop(0)
        if left != 'null':
            node.left = TreeNode(left)
            queue.append(node.left)
        if not lista:
            break
        right = lista.pop(0)
        if right != 'null':
            node.right = TreeNode(right)
            queue.append(node.right)

    return root


lista = [1, 2, 3]
lista = [-10, 9, 20, 'null', 'null', 15, 7]
lista=[2,-1]
root = list2TreeNode(lista)
res = Solution().maxPathSum(root)
print(res)
