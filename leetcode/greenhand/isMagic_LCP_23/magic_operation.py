"""
author:wjw
功能：实现magic操作
"""


class Solution:
    def magic_operation(self, n, k):
        out = []

        l = list(range(1, n))
        while l:
            l2 = l[0:n:2]
            l3 = l[1::2]
            l = l3 + l2
            for i in range(k):
                if l:
                    out.append(l.pop(0))

        return out


n = 6
k = 3
res = Solution().magic_operation(n, k)
print(res)
