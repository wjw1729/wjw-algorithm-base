"""
author:wjw
customized clean function
应该可以通过两次比遍历可以确定消除的边界。（前后）
可以用栈来做.
"""


def clean(s):
    s = s + '#'
    stack = []

    for ch in s:
        if stack and stack[-1][0] != ch and stack[-1][1] >= 2:
            i = stack[-1][1]
            while i >= 0:
                stack.pop()
                i -= 1

        if stack and stack[-1][0] == ch:
            stack.append((ch, stack[-1][1] + 1))
        else:
            stack.append((ch, 0))

    return ''.join(x[0] for x in stack[:-1])


s = 'RRWWRRBBBRWR'
res = clean(s)
print(res)
