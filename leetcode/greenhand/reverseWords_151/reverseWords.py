"""
author:wjw
分析：s.split()对空格进行分割，多个空格视为一个空格！
"""


class Solution:
    def reverseWords(self, s):
        ls = s.split()

        return ' '.join(reversed(ls))


s = "a good   example"
res = Solution().reverseWords(s)
print(res)
