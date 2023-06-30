"""
author:
分析：单调栈+
时间复杂度：O（n）
"""

from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s):

        counter = defaultdict(int)
        stack = []

        for char in s:
            counter[char] += 1

        for char in s:
            if char not in stack:
                while stack and char < stack[-1] and counter[stack[-1]] > 0:
                    stack.pop()

                stack.append(char)

            counter[char] -= 1

        return ''.join(stack)


s = "bcabc"
s = "cbacdcbc"
s = "abacb"

res = Solution().removeDuplicateLetters(s)
print(res)
