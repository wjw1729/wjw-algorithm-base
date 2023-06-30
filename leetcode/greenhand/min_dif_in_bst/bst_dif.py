# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        min_dif=1000000000
        for node in TreeNode:
            dif=tree_successor(node)-node.value
            if dif < min_dif:
                min_dif=dif

        return min_dif


def tree_minimum(x):
    while x.left!=None:
        x=x.left
        return x



def tree_successor(x):
    if x.right!=None:
        return tree_minimum(x)
    y= x.p
    while y!=None and x==y.right:
        x=y
        y= y.p
        return y


