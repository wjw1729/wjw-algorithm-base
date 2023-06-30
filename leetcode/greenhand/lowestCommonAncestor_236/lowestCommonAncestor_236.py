"""
author:wjw
分析：深度优先搜索
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = []
        bin = set()

        def backtrack(root, path):
            if root not in bin and (root == p or q):
                ans.append(path + [root])
                bin.add(root)

            if len(ans) == 2:
                return

            path.append(root)
            if root.left != None:
                backtrack(root.left, path)
                if path != []:
                    path.pop()

            if root.left != None:
                backtrack(root.right, path)
                if path != []:
                    path.pop()

        backtrack(root, [])

        while ans[1]:
            node = ans[1].pop()
            if node in ans[0]:
                return node
