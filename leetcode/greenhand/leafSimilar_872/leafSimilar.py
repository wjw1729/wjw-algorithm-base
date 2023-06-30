"""
author:wjw
分析：按照回溯的思路，进行left，right的依次搜索
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf(root):
    # leaf = []
    # nodelist = [root]
    # i = 0
    #
    # while i < len(nodelist):
    #     node = nodelist[i]
    #     if node.left == None and node.right == None:
    #         leaf.append(node.val)
    #     if node.left != None:
    #         nodelist.append(node.left)
    #
    #     if node.right != None:
    #         nodelist.append(node.right)
    #     i += 1
    # return leaf

    leaf = []

    def dfs(node):
        if node.left == None and node.right == None:
            leaf.append(node.val)
            return
        if node.left != None:
            dfs(node.left)

        if node.right != None:
            dfs(node.right)

    dfs(root)
    return leaf


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if leaf(root1) == leaf(root2):
            return True
        else:
            return False


def list2TreeNode(l):
    root = TreeNode(int(l[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(l):
        node = nodeQueue[front]
        front = front + 1

        item = l[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(l):
            break

        item = l[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


root1 = [3, 5, 1, 6, 2, 9, 8, 'null', 'null', 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, 'null', 'null', 'null', 'null', 'null', 'null', 9, 8]
root1 = [1, 2, 3]
root2 = [1, 3, 2]
# root1=[119,113,'null',11,30,43,76,15,60,67,74]
# root2=[11,69,60,115,66,15,60,67,74,'null',76]

root1 = list2TreeNode(root1)
root2 = list2TreeNode(root2)
res = Solution().leafSimilar(root1, root2)
print(res)
