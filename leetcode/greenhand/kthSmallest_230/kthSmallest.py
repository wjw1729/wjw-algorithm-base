"""
author:wjw
分析：中序遍历。递归实现。
"""

class Solution:
    def kthSmallest(self,root,k):
        def inorder(root):
            if not root:
                return []
            else:
                return inorder(root.left)+[root.val]+inorder(root.right)

        inorderls=inorder(root)
        return inorderls[k-1]
