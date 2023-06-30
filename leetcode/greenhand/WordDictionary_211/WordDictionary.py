"""
author:wjw
分析：字典树的创建，添加字符和查找字符。
深度优先搜索匹配。以及字符串构成的尾节点标记。
"""


class Trie:
    serial: str = ''
    children: dict

    def __init__(self):
        self.children = dict()


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.serial = word

    def search(self, word: str) -> bool:
        n = len(word)
        cur = self.root

        def dfs(node, i):

            if i == n:
                if node.serial != '':
                    return True
                else:
                    return False

            res = False

            if word[i] == '.':
                for k, v in node.children.items():
                    res |= dfs(v, i + 1)

            elif word[i] in node.children:
                res |= dfs(node.children[word[i]], i + 1)

            return res

        return dfs(cur, 0)


obj = WordDictionary()
obj.addWord('abc')
print(obj.search('ab'))
