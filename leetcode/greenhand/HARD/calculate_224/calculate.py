"""
author:wjw
分析：括号类题。
"""


class Solution:
    def calculate(self, s):
        s=s.replace(' ','')
        stack = []
        part = 0
        n = len(s)
        i = 0
        num = ''
        sign = 1

        while i < n:
            if s[i] == '(':
                stack.append(('(', sign, part))
                part = 0
                sign=1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == ')':
                _, sign, prepart = stack.pop()
                part = prepart + sign * part
            else:
                while i < n and s[i].isdigit():
                    num += s[i]
                    i += 1
                num = int(num)
                part += sign * num
                num = ''
                continue

            i += 1
        return part


s = "1+1"
s=" 2-1 + 2 "
s= "(1+(4+5+2)-3)+(6+8)"
s="- (3 + (4 + 5))"
res = Solution().calculate(s)
print(res)
