"""
author；wjw
分析:s
"""

from collections import Counter
from sortedcontainers import SortedList

def f(s):
    d = Counter(s)
    res=d[min(d.keys())]
    return res


class Solution:
    def numSmallerByFrequency(self, queries, words):

        n = len(queries)
        m=len(words)
        fq=[]
        fw=SortedList()
        res = [0] * n
        for i in range(n):
            fq.append(f(queries[i]))

        for j in range(m):
            fw.add(f(words[j]))



        for i in range(n):
            idx=fw.bisect_right(fq[i])
            res[i]=m-idx


        return res


queries = ["cbd"]
words = ["zaaaz"]
queries = ["bbb", "cc"]
words = ["a", "aa", "aaa", "aaaa"]
queries = ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
words = ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]
result = Solution().numSmallerByFrequency(queries, words)
print(result)
