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
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        ans = []

        while queue:
            ans.append([x.val for x in queue])
            nextqueue = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    nextqueue.append(node.left)
                if node.right:
                    nextqueue.append(node.right)
            queue = nextqueue

        return ans


def list2Tree(lista):
    root = TreeNode(lista.pop(0))

    queue = [root]
    while lista:
        node = queue.pop(0)
        l = lista.pop(0)
        if l != 'null':
            node.left = TreeNode(l)

        if not lista:
            break
        r = lista.pop(0)
        if r != 'null':
            node.right = TreeNode(r)
    return root

l=[1,2]
root=list2Tree(l)
res=Solution().levelOrder(root)
print(res)