"""
author:wjw
分析：
"""


class Solution:
    def longestValidParentheses(self, s):
        s=s.rstrip('(')
        n = len(s)
        stack = []
        ans = 0
        total = 0
        for i in range(n):
            if s[i] == ')':
                if stack == []:
                    ans = max(ans, total)
                    total = 0
                else:
                    _,num=stack.pop()
                    total += 2+num
            if s[i] == '(':
                if s[i-1]=='(':
                    stack.append(('(',0))
                else:
                    stack.append(('(',total))
                    ans=max(ans,total)
                    total=0




        ans = max(ans, total)

        return ans


s = '(()()()()))()'
#s="()(()"
#s=")()())()()("
#s="(())()(()(("
res = Solution().longestValidParentheses(s)
print(res)
