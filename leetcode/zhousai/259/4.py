"""
"""

from collections import Counter
from itertools import permutations

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) :
            num = Counter(s)
            hot = ''.join(ele * (num[ele] // k) for ele in sorted(num, reverse=True))
            for i in range(len(hot), 0, -1):
                for item in permutations(hot, i):
                    word = ''.join(item)
                    ss = iter(s)
                    if all(c in ss for c in word * k):
                        return word
            return ''

s = "letsleetcode"
k = 2
res=Solution().longestSubsequenceRepeatedK(s,k)
print(res)