"""
author:wjw
分析：跟正向统计不同的是，这里采取在counter_t基础上进行相减的操作，其实思路是一样的。就是理解起来和边界条件书写起来可能有点困难。
"""
from collections import defaultdict


class Solution:
    def minWindow(self, s, t):

        n = len(s)
        counter_t = defaultdict(int)
        for each_t in t:
            counter_t[each_t] += 1
        tlen = len(t)

        mlleft, mlright = 0, n
        l = 0
        for r in range(n):
            if counter_t[s[r]] > 0:
                tlen -= 1
            counter_t[s[r]] -= 1

            if tlen == 0:
                while counter_t[s[l]] < 0:
                    counter_t[s[l]] += 1
                    l += 1

                if r - l < mlright - mlleft:
                    mlleft, mlright = l, r

                counter_t[s[l]] += 1
                tlen += 1
                l += 1

        return s[mlleft:mlright + 1] if mlright != n else ''


s = "ADOBECODEBANC"
t = "ABC"
res = Solution().minWindow(s, t)
print(res)
