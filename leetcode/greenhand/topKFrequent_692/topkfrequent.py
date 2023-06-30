"""
author:wjw
分析：反转字典.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, words, k: int):
        d = Counter(words)
        d1 = {}
        for key, v in d.items():
            if v not in d1.keys():
                d1[v] = [key]
                continue
            d1[v].append(key)

        ans = []
        l1 = list(d1.keys())
        l1.sort(reverse=True)
        for i in l1:
            ans += sorted(d1[i])

        return ans[:k]


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
res = Solution().topKFrequent(words, k)
print(res)
