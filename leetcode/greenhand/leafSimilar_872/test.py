

def leaf(root):
    leaf = []

    def dfs(node):
        if node.left==None and node.right==None:
            leaf.append(node.val)
            return
        if node.left!=None:
            dfs(node.left)
        else:
            return
        if node.right!=None:
            dfs(node.right)
        else:
            return

    dfs(root)
    return leaf

