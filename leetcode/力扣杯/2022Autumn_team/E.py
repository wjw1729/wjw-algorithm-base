# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def minSupplyStationNumber(self, root) -> int:

        @lru_cache(None)
        def dfs(node,pst,pst1):

            if not node:
                if pst==pst1==0:

                    return float('inf')
                else:
                    return 0


            res=float('inf')
            for ns in range(1,-1,-1):
                if ns==1:
                    res=min(res,dfs(node.left,ns,pst)+dfs(node.right,ns,pst)+1)
                else:
                    res=min(res,dfs(node.left,ns,pst)+dfs(node.right,ns,pst))
                if pst==pst1==0:
                    break

            return res



        a1=dfs(root,0,-1)


        print(a1)
        return a1



