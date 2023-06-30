"""
author:wjw
分析：递推执行即可。。。。
"""


def trans(s):
    s1 = ''
    num = 0
    for i in range(len(s)):
        if i == 0:
            last = s[0]
        now = s[i]
        if now == last:
            num += 1
        else:
            s1 += str(num) + last
            num = 1
        if i == len(s) - 1:
            s1 += str(num) + now

        last = now
    return s1


class Solution:
    def countAndSay(self, n):
        s = '1'
        for i in range(n - 1):
            s = trans(s)
        return s


n = 4
res = Solution().countAndSay(n)
print(res)
