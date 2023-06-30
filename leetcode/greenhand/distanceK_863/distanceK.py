"""
author:wjw
分析：距离目标结点距离为k的结点为以其为根节点的深度为k的子节点，以及其父节点在另一颗子树上深度为k-1的子节点。以此类推。
    在树中查找目标结点的路径。在该路径中依次从目标节点网上查找父节点树的k-i深度的结点，但是查找过程记得避开目标路径上的点。
"""


class Solution:
    def distanceK(self, root, target, k):

        self.ans = []
        self.check = False

        def dfs(root, path):

            if self.check:
                return
            if not root:
                return

            if root.val == target:
                self.check = True
                self.ans = path + [root]
                return

            dfs(root.left, path + [root])
            dfs(root.right, path + [root])

        dfs(root, [])

        self.res = []

        for i in range(min(k + 1, len(self.ans))):

            root = self.ans[-(i + 1)]
            queue = [root]

            tmpk = k - i
            if tmpk == 0:
                self.res += [x.val for x in queue]
            while queue:
                nextqueue = []
                while queue:
                    node = queue.pop(0)
                    if node.left and node.left not in self.ans:
                        nextqueue.append(node.left)
                    if node.right and node.right not in self.ans:
                        nextqueue.append(node.right)
                tmpk -= 1
                if tmpk == 0:
                    break
                queue = nextqueue
            self.res += [x.val for x in nextqueue]

        return self.res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list2tree(lista):
    root = TreeNode(lista.pop(0))
    queue = [root]

    while lista:
        node = queue.pop(0)

        tmp = lista.pop(0)
        if tmp != 'null':
            node.left = TreeNode(tmp)
            queue.append(node.left)
        if not lista:
            break

        tmp = lista.pop(0)
        if tmp != 'null':
            node.right = TreeNode(tmp)
            queue.append(node.right)

    return root


ls = [0, 1, "null", 3, 2]
root = list2tree(ls)
res = Solution().distanceK(root, 2, 1)
print(res)
