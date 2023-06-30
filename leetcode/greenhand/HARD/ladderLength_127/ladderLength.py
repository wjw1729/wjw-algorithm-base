"""
author:wjw
分析：深度优先搜索+哈希表表示相邻关系。
"""
import time
from collections import defaultdict


def computedis(s1, s2):
    n = len(s1)
    ans = 0
    for i in range(n):
        if s1[i] != s2[i]:
            ans += 1
    return ans == 1


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        self.ans = float('inf')

        if endWord not in wordList:
            return 0

        adjacent = defaultdict(list)

        n = len(wordList)

        for i in range(n):
            if computedis(beginWord, wordList[i]):
                adjacent[beginWord].append(wordList[i])
            for j in range(i + 1, n):
                if computedis(wordList[i], wordList[j]):
                    adjacent[wordList[i]].append(wordList[j])
                    adjacent[wordList[j]].append(wordList[i])

        def dfs(word, path):
            if word == endWord:
                self.ans = min(self.ans, len(path) + 1)
                print(path)
                return

            for next in adjacent[word]:
                if next not in path:
                    dfs(next, path + [word])

        dfs(beginWord, [])
        return self.ans


t1 = time.time()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "qa"
endWord = "sq"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci",
            "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
            "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
            "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
            "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
            "pa", "he", "lr", "sq", "ye"]
res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)
print(time.time() - t1)
