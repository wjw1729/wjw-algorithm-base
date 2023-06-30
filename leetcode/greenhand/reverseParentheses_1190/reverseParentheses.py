"""
author:wjw
分析：括号反转，依次从外到内。注意选择括号要注意配对。
"""


# 单次反转
def delete_br(s):
    left = 0
    while s[left] != '(':
        left += 1

    right = left
    layer = -1
    while s[right] != ')' or layer != 0:
        if s[right] == '(':
            layer += 1
        if s[right] == ')':
            layer -= 1
        right += 1

    x = ''.join(list(reversed(s[left + 1:right])))
    x = x.replace('(', '#')
    x = x.replace(')', '(')
    x = x.replace('#', ')')
    return s[:left] + x + s[right + 1:]


class Solution:
    def reverseParentheses(self, s):
        while '(' in s:
            s = delete_br(s)
        return s


s = "a(bcdefghijkl(mno)p)q"
# s = "ta()usw((((a))))"
res = Solution().reverseParentheses(s)
print(res)
