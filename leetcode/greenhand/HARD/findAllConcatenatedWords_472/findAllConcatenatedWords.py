"""
字典树+深度优先搜索

"""


class Trie():
    def __init__(self, v=''):
        self.children = dict()
        self.val = v
        self.word = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        root = Trie()

        words.sort(key=lambda x: len(x))

        def dfs(s, node):
            if s == '':
                if node.word:
                    return True

            elif s[0] in node.children:
                if node.children[s[0]].word == True and dfs(s[1:], root):
                    return True

                if dfs(s[1:], node.children[s[0]]):
                    return True

            return False

        ans = []
        for wrd in words:
            if dfs(wrd, root):
                ans.append(wrd)
            else:
                node = root
                for c in wrd:
                    if c not in node.children:
                        node.children[c] = Trie(c)
                    node = node.children[c]
                node.word = True

        return ans


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

res = Solution().findAllConcatenatedWordsInADict(words)
print(res)
