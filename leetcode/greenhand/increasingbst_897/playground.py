# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def midfirst(tree):
    res = [tree.val]
    if tree.left != None:
        res = midfirst(tree.left) + res
    if tree.right != None:
        res = res + midfirst(tree.right)
    return res


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l1 = midfirst(root)

        rootnode = TreeNode(l1[0])
        node=rootnode
        index = 1
        while index < len(l1):
            node.left = None
            node.right = TreeNode(l1[index])
            node = node.right
            index = index + 1
        return rootnode


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io

    line='[5,3,6,2,4,null,8,1,null,null,null,7,9]'
    while True:
        try:
            #line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().increasingBST(root)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()