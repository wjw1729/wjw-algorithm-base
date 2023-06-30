"""
author:wjw
分析：滑动窗口。标准解法。
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        n = len(s)
        minlen = n
        charset = set(t)
        counter_t = {}
        for each_t in t:
            counter_t.setdefault(each_t, 0)
            counter_t[each_t] += 1

        counter_s = defaultdict(int)
        l = 0
        r = 0
        ans = ()
        check = False
        while r < n:
            while r < n and not all(counter_s[key] >= counter_t[key] for key in counter_t.keys()):
                if s[r] in charset:
                    counter_s.setdefault(s[r], 0)
                    counter_s[s[r]] += 1
                r += 1

            while all(counter_s[key] >= counter_t[key] for key in counter_t.keys()):
                check = True
                if s[l] in charset:
                    counter_s[s[l]] -= 1

                l += 1
            if check and r - l < minlen:
                ans = (l, r)
                minlen=r-l

        return s[ans[0] - 1:ans[1]] if ans else ""


s = "ADOBECODEBANC"
t = "ABC"
"""
s = "a"
t = "a"
"""
res = Solution().minWindow(s, t)
print(res)
