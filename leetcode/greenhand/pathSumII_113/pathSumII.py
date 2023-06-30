"""
author:wjw
分析：回溯
"""


class Solution:
    def pathSum(self, root, targetSum):

        if root==None:
            return []
        ans = []

        def backtrack(node, path):

            if node.left == None and node.right == None:
                if sum(path) == targetSum:
                    ans.append(path)
                    return

            if node.left != None:
                backtrack(node.left, path + [node.left.val])

            if node.right != None:
                backtrack(node.right, path + [node.right.val])

        backtrack(root, [root.val])
        return ans
