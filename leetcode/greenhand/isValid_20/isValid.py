"""
author:wjw
分析：遇到括号的题目，首先就应该想到栈。
"""


class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        d = {')': '(',
             ']': '[',
             '}': '{'}

        stack = []

        for char in s:
            if char in d:
                if stack[-1] != d[char]:
                    return False

                stack.pop()
            else:
                stack.append(char)

        return True


s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
res = Solution().isValid(s)
print(res)
