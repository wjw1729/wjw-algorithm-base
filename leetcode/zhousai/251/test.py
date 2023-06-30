class Trie:
    serial: str = ""
    children: dict

    def __init__(self):
        self.children = {}


from collections import defaultdict


class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq = defaultdict(int)

        def construct(node):
            if not node.children:
                return

            tmp = []
            for folder, child in node.children.items():
                construct(child)
                tmp.append(folder + '(' + child.serial + ')')
            tmp.sort()
            node.serial = ''.join(tmp)
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
paths = [["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]

res = Solution().deleteDuplicateFolder(paths)
print(res)
