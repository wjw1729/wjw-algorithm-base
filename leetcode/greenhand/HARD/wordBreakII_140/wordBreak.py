"""
author:wjw
分析：回溯算法
"""


class Solution:
    def wordBreak(self, s, wordDict):
        ans = []

        def backtrack(s, split_ls):

            if s == "":
                ans.append(' '.join(split_ls))
                return

            for word in wordDict:
                wlen = len(word)
                if s[:wlen] == word:
                    split_ls.append(word)
                    tmp = s
                    s = s[wlen:]
                    backtrack(s, split_ls)

                    s = tmp
                    split_ls.pop()

        backtrack(s, [])
        return ans


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
res = Solution().wordBreak(s, wordDict)
print(res)
