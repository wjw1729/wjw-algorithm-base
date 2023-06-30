"""
author:unknown
分析：用栈实现
"""


class Solution:
    def reverseParentheses(self, s):
        stack = [[]]
        for i, c in enumerate(s):
            if c == "(":
                stack.append([])
            elif c == ')':
                t = stack.pop()
                stack[-1] += t[::-1]
            else:
                stack[-1].append(c)
        return ''.join(stack[0])
