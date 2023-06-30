"""
author:wjw
分析：将一棵树编码为如下结构：（root.left）+root+(root.right).如果遇到空结点就返回'X'
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree  to a single string.

        :type root:TreeNode
        :rtype :str
        """
        if not root:
            return 'X'
        lefttree = '(' + self.serialize(root.left) + ')'
        righttree = '(' + self.serialize(root.right) + ')'

        return lefttree + str(root.val) + righttree

    def deserialzie(self, data):
        """Decodes your encoded data here.

        :param data:str
        :return:TreeNode
        """

        self.ptr = 0

        def parse():

            if data[self.ptr] == 'X':
                self.ptr += 1
                return None
            cur = TreeNode(0)
            cur.left = parseSubtree()
            cur.val = parseInt()
            cur.right = parseSubtree()
            return cur

        def parseSubtree():

            self.ptr += 1
            subtree = parse()
            self.ptr += 1
            return subtree

        def parseInt():

            x, sign = 0, 1
            if data[self.ptr] == '-':
                sign = -1
                self.ptr += 1

            while data[self.ptr].isdigit():
                x = x * 10 + int(data[self.ptr])
                self.ptr += 1

            return x * sign

        return parse()


def list2root(lista):
    root = TreeNode(0)
    root.val = lista.pop(0)
    queue = [root]

    while lista:
        node = queue.pop(0)
        tmp = lista.pop(0)
        if tmp != 'null':
            node.left = TreeNode(tmp)
            queue.append(node.left)

        tmp = lista.pop(0)
        if tmp != 'null':
            node.right = TreeNode(tmp)
            queue.append(node.right)

    return root


lista = [1, 2, 3, 'null', 'null', 4, 5]
root = list2root(lista)
ser = Codec().serialize(root)
ans = Codec().deserialzie(ser)
print(root)
print(ser)
print(ans)
