"""
author:wjw
分析：
"""
from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        ans = []
        n = len(s)
        wordlen = len(words[0])
        wordset = set(words)
        originset=wordset.copy()
        counter = Counter(words)
        slidecounter = counter.copy()

        for i in range(n):

            if s[i:i + wordlen] in wordset:
                slidecounter[s[i:i + wordlen]] -= 1
                if slidecounter[s[i:i + wordlen]] == 0:
                    slidecounter.pop(s[i:i + wordlen])
                    wordset.remove(s[i:i + wordlen])
                j = i + wordlen
                while s[j:j + wordlen] in wordset:
                    slidecounter[s[j:j + wordlen]] -= 1
                    if slidecounter[s[j:j + wordlen]] == 0:
                        slidecounter.pop(s[j:j + wordlen])
                        wordset.remove(s[j:j+wordlen])
                    j=j+wordlen

                if slidecounter == {}:
                    ans.append(i)
                slidecounter = counter.copy()
                wordset=originset.copy()

        return ans


s = "barfoothefoobarman"
words = ["foo", "bar"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
res = Solution().findSubstring(s, words)
print(res)
