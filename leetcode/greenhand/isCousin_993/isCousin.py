"""
author:wjw
分析：深度相同，父节点不同.建立node到dpeth的映射关系。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list2TreeNode(input):
    root = TreeNode(input[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodeQueue[front]
        front = front + 1

        item = input[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(input):
            break

        item = input[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth = {}
        flow = [root]
        depth[root.val] = 0

        for node in flow:

            if node.left != None and node.right != None:
                if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                    return False

            if node.left != None:
                flow.append(node.left)
                depth[node.left.val] = depth[node.val] + 1

            if node.right != None:
                flow.append(node.right)
                depth[node.right.val] = depth[node.val] + 1

        if depth[x] == depth[y]:
            return True
        else:
            return False


input = [1, 2, 3, 'null', 4, 'null', 5]
input = [1, 2, 3, 'null', 4]
root = list2TreeNode(input)
res = Solution().isCousins(root, 2, 3)
print(res)
