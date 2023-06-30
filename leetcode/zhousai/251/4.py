"""
author:wjw
分析：前缀知识：二叉树的序列化与反序列化297。
    多叉字典树的构建。{folder：child}其中folder是节点值，child是节点。

"""


class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        self.children = dict()


from collections import Counter


class Solution:
    def deleteDuplicateFolder(self, paths):

        root = Trie()
        ###构建多叉字典树
        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq = Counter()

        def construct(node):####构建serial属性，以及freq的哈希表
            if not node.children:
                return
            v = list()

            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")

            v.sort()
            node.serial = ''.join(v)
            freq[node.serial] += 1

        construct(root)
        ans = []
        path = []

        def operate(node):
            if freq[node.serial] > 1:
                return

            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans


paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
"""
paths = [["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]
paths = [["a", "b"], ["c", "d"], ["c"], ["a"]]
paths = [["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"]]
paths = [["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"], ["b", "w"]]
"""

res = Solution().deleteDuplicateFolder(paths)
print(res)
