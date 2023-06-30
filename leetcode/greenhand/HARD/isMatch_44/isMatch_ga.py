"""
author:wjw
分析：自己写一遍。
"""


class Solution:
    def isMatch(self, s, p):
        def allstar(st, left, right):
            return all(st[i] == '*' for i in range(left, right))

        def charMatch(s1, s2):
            return s1 == s2 or s2 == '?'

        s_right = len(s)
        p_right = len(p)

        while s_right > 0 and p_right > 0 and p[p_right - 1] != '*':
            if charMatch(s[s_right - 1], p[p_right - 1]):
                s_right -= 1
                p_right -= 1
            else:
                return False

        if p_right == 0:
            return s_right == 0

        s_index, p_index = 0, 0
        s_record, p_record = -1, -1

        while s_index < s_right and p_index < p_right:
            if p[p_index] == '*':
                s_record = s_index
                p_index += 1
                p_record = p_index

            elif charMatch(s[s_index], p[p_index]):
                s_index += 1
                p_index += 1
            elif s_record != -1 and s_record + 1 < s_right:
                s_record += 1
                s_index = s_record
                p_index = p_record
            else:
                return False

        return allstar(p, p_index, p_right)


s = "aa"
p = "*"

# s = "cb"
# p = "?a"
# s = "adceb"
# p = "*a*b"

# s = "acdcb"
# p = "a*c?b"
s = "mississippi"
p = "m??*ss*?i*pi"
res = Solution().isMatch(s, p)
print(res)
