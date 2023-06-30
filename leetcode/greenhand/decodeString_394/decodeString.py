"""
author:wjw
分析：
"""


class Solution:
    def decodeString(self, s):
        n = len(s)
        stack = []
        ans = ''
        part = ''
        i = 0
        num = ''
        while i < n:
            while s[i].isdigit():
                num += s[i]
                i += 1
            if num.isdigit():
                num = int(num)
            if s[i] == '[':
                stack.append(('[', num, part))
                num = ''
                part = ''
            if s[i].isalpha():
                part += s[i]

            if s[i] == ']':
                _, multi, prepart = stack.pop()
                if stack:
                    part = prepart + part * multi
                else:
                    ans += prepart + part * multi
                    part = ''
            i += 1
        ans += part
        return ans


s = "3[a]2[bc]"
#s = "3[a2[c]]"
#s = "abc3[cd]xyz"
res = Solution().decodeString(s)
print(res)
