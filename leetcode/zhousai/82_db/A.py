class Solution:
    def evaluateTree(self, root) -> bool:

        @lru_cache(None)
        def dfs(node):
            if not node.left and not node.right:
                return bool(node.val)

            l=dfs(node.left)
            r=dfs(node.right)
            if node.val==2:
                return l or r

            else:
                return  l and r

        return dfs(root)