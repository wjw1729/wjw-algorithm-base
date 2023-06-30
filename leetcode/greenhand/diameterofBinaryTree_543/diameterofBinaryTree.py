"""
author:wjw
分析:深度优先搜索.
"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def diameterofBinaryTree(self,root):
        self.ans=1

        def dnode(root):
            if not root:
                return 0

            L=dnode(root.left)
            R=dnode(root.right)

            self.ans=max(self.ans,L+R+1)

            return max(L,R)+1

        dnode(root)
        return self.ans-1


