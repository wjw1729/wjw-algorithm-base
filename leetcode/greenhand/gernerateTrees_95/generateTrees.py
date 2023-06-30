"""
author:wjw
分析：递归实现。在已知左子树列表和右子树列表的情况下，构建当前树。
    dfs：从输入结点值组成的列表中返回所有可能的树。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):

        def dfs(nodels):
            if nodels == []:
                return [None]
            if len(nodels) == 1:
                return [TreeNode(nodels[0])]

            res = []
            for val in nodels:
                left = [x for x in nodels if x < val]
                right = [x for x in nodels if x > val]

                left_tree = dfs(left)
                right_tree = dfs(right)

                for left_root in left_tree:
                    for right_root in right_tree:
                        root = TreeNode(val)
                        root.left = left_root
                        root.right = right_root
                        res.append(root)
            return res

        ans = dfs(list(range(1, n + 1)))
        return ans


n = 3
res = Solution().generateTrees(n)
print(res)
