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
                self.ans = path+[root]
                return

            dfs(root.left, path+[root])

            dfs(root.right, path+[root])

        dfs(root, [])
        return self.ans


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
