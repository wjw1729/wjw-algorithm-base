"""
author:wjw
分析：先序遍历即可。
"""
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leftfirst(root):
    res = [root.val]
    if root.left != None:
        res = leftfirst(root.left) + res
    if root.right != None:
        res = res + leftfirst(root.right)
    return res


def list2Treenode(input):
    root = TreeNode(input[0])
    nodequeue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodequeue[front]
        front += 1

        if input[index] != 'null':
            node.left = TreeNode(input[index])
            nodequeue.append(node.left)
        index = index + 1

        if index >= len(input):
            break

        if input[index] != 'null':
            node.right = TreeNode(input[index])
            nodequeue.append(node.right)
        index = index + 1

    return root


class Solution:
    def rangeSumBST(self, root, low, high):
        l1 = leftfirst(root)

        idx1 = bisect.bisect_left(l1, low)
        idx2 = bisect.bisect_right(l1, high)
        ans = sum(l1[idx1:idx2])

        return ans


root = [10, 5, 15, 3, 7, 'null', 18]
root = [10, 5, 15, 3, 7, 13, 18, 1, 'null', 6]
root = list2Treenode(root)
low = 6
high = 10
res = Solution().rangeSumBST(root, low, high)
print(res)
