"""
author:wjw
分析：
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        ans = [str(root.val)]
        while queue:
            node = queue.pop(0)
            if node.left == None:
                ans.append('null')
            else:
                ans.append(str(node.left.val))
                queue.append(node.left)

            if node.right == None:
                ans.append('null')
            else:
                ans.append(str(node.right.val))
                queue.append(node.right)
        return ans
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

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


def main():
    import sys
    import io

    while True:
        try:
            line ='[1,2,3,null,null,4,5]'
            root = stringToTreeNode(line);

            ret = Codec().serialize(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
