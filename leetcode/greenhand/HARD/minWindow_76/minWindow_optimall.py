"""
author:wjw
分析：可以将无关字符提前进行处理掉。
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s, t):

        counter_t = defaultdict(int)

        for each_t in t:
            counter_t[each_t] += 1
        tlen = len(t)
        tset = set(t)
        s_en = list(enumerate(s))
        n = len(s)

        for i, char in reversed(s_en):
            if char not in tset:
                s_en.pop(i)

        minleft, minright = 0, n
        l = 0
        for r, char in s_en:
            if counter_t[char] > 0:
                tlen -= 1
            counter_t[char] -= 1

            if tlen == 0:
                while counter_t[s_en[l][1]] < 0:
                    counter_t[s_en[l][1]] += 1
                    l += 1

                if r - s_en[l][0] < minright - minleft:
                    minleft, minright = s_en[l][0], r

                counter_t[s_en[l][1]] += 1
                tlen += 1
                l += 1

        return s[minleft:minright + 1] if minright != n else ""


s = "ADOBECODEBANC"
t = "ABC"
res = Solution().minWindow(s, t)
print(res)
